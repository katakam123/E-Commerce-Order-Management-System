from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.auth import UserRegister, UserLogin
from app.auth.jwt import (
    hash_password,
    verify_password,
    create_access_token
)


def register_user(db: Session, user_data: UserRegister):

    existing_user = db.query(User).filter(
        User.email == user_data.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    user = User(
        name=user_data.name,
        email=user_data.email,
        hashed_password=hash_password(user_data.password),
        role="customer"
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def login_user(db: Session, user_data: UserLogin):

    user = db.query(User).filter(
        User.email == user_data.email
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(
        user_data.password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        {
            "sub": str(user.id),
            "role": user.role
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }