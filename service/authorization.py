from service import db as db_service


async def registration(
        db,
        login,
        password
):
    return await db_service.registration(
        db,
        login,
        password
    )


async def token_check(active_token):
    return await db_service.token_check(active_token)


async def auth(
        login,
        refresh_token
):
    return await db_service.auth(
        login,
        refresh_token
    )
