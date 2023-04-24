from fastapi import APIRouter, Depends
from schemas.authorization_schema import (
    SignInInputInfo, TestInputInfo, LogInInputInfo,
    SingInOutputInfo, TestOutputInfo, LogInOutputInfo
)
from service import authorization
from sqlalchemy.ext.asyncio import AsyncSession
from crud import get_db

router = APIRouter()

@router.post('/sign_in/', response_model=SingInOutputInfo)
async def registration(
    sign_in: SignInInputInfo,
    db: AsyncSession = Depends(get_db),
) -> SingInOutputInfo:
    try:
        server_response: SingInOutputInfo = await authorization.registration(db, sign_in.login, sign_in.password)
        return server_response
    except:
        except_response = {"code": 415, "msg": "Unsupported Media Type"}
        return except_response


@router.post('/test_token_expired/', response_model=TestOutputInfo)
async def token_check(
    test_token_expired: TestInputInfo,
    db: AsyncSession = Depends(get_db),
) -> TestOutputInfo:
    try:
        server_response: TestOutputInfo = await authorization.token_check(db, test_token_expired.login, test_token_expired.refresh_token)
        return server_response
    except:
        except_response = {"code": 415, "msg": "Unsupported Media Type"}
        return except_response

@router.post('/log_in/', response_model=LogInOutputInfo)
async def auth(
    log_in: LogInInputInfo
) -> LogInOutputInfo:
    try:
        server_response: LogInOutputInfo = await authorization.auth(log_in.login, log_in.active_token)
        return server_response
    except:
        except_response = {"code": 415, "msg": "Unsupported Media Type"}
        return except_response