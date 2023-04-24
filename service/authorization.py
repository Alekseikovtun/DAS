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


async def token_check(
        db,
        login,
        refresh_token
):
    return await db_service.token_check(
        db,
        login,
        refresh_token
    )


async def auth(
        login,
        active_token
):
    return await db_service.auth(
        login,
        active_token
    )
