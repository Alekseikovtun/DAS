from fastapi import APIRouter
from schemas.authorization_schema import (
    SignInInputInfo, TestInputInfo, LogInInputInfo,
    SingInOutputInfo, TestOutputInfo, LogInOutputInfo
)
from service import authorization

router = APIRouter()

@router.post('/sign_in/', response_model=SingInOutputInfo)
async def registration(
    sign_in: SignInInputInfo
) -> SingInOutputInfo:
    server_response: SingInOutputInfo = await authorization.registration(sign_in.login, sign_in.password)
    return server_response

@router.post('/test_token_expired/', response_model=TestOutputInfo)
async def token_check(
    test_token_expired: TestInputInfo
) -> TestOutputInfo:
    server_response: TestOutputInfo = await authorization.token_check(test_token_expired.active_token)
    return server_response

@router.post('/log_in/', response_model=LogInOutputInfo)
async def auth(
    log_in: LogInInputInfo
) -> LogInOutputInfo:
    server_response: LogInOutputInfo = await authorization.auth(log_in.login, log_in.refresh_token)
    return server_response