import asyncio
import functools


def async_retry(max_attempts: int = 3, base_delay: float = 1.0):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return await func(*args, **kwargs)
                except asyncio.CancelledError:
                    raise
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    delay = base_delay * (2**attempt)
                    print(
                        f"Tentativa {attempt + 1} falhou. Tentando novamente em {delay}s..."
                    )
                    await asyncio.sleep(delay)

        return wrapper

    return decorator
