from fastapi import Depends, HTTPException, status

from app.middleware.auth_middleware import get_current_user

from app.core.logger import logger


class PermissionChecker:

    def __init__(self, required_permissions: list):

        self.required_permissions = required_permissions

    def __call__(self, current_user=Depends(get_current_user)):

        user_permissions = current_user.get("permissions", [])

        has_permission = any(

            permission in user_permissions

            for permission in self.required_permissions

        )

        if not has_permission:

            logger.warning(f"PERMISSION_DENIED | " f"user_id={current_user.get('user_id')} | " f"required={self.required_permissions}")

            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Permission denied")

        logger.info(f"PERMISSION_GRANTED | " f"user_id={current_user.get('user_id')}")

        return current_user