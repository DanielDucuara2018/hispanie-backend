from typing import List

from fastapi import APIRouter, Depends, HTTPException

from hispanie.schema import AccountResponse

from ...action import (
    create_business,
    delete_business,
    get_current_account,
    read_businesses,
    update_business,
)
from ...schema import BusinessCreateRequest, BusinessResponse, BusinessUpdateRequest

router = APIRouter(
    prefix="/businesses",
    tags=["businesses"],
    responses={404: {"description": "Not found"}},
)


# Create Business
@router.post("", response_model=BusinessResponse)
async def create(
    business_data: BusinessCreateRequest,
    current_account: AccountResponse = Depends(get_current_account),
):
    """
    Create a new business for the authenticated account.
    """
    try:
        return create_business(business_data, current_account.id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating business: {str(e)}")


# Read Business
@router.get("", response_model=List[BusinessResponse])
async def read(
    current_account: AccountResponse = Depends(get_current_account),
):
    """
    Retrieve all business for the authenticated account.
    """
    try:
        return read_businesses(account_id=current_account.id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error retrieving business: {str(e)}")


# Update Business
@router.put("/{event_id}", response_model=BusinessResponse)
async def update(
    business_id: str,
    business_update: BusinessUpdateRequest,
    current_account: AccountResponse = Depends(get_current_account),
):
    """
    Update an business by its ID. The business must belong to the current account.
    """
    try:
        return update_business(business_id, current_account.id, business_update)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error updating event: {str(e)}")


# Delete Business
@router.delete("/{event_id}", response_model=BusinessResponse)
async def delete(
    business_id: str,
    current_account: AccountResponse = Depends(get_current_account),
):
    """
    Delete an business by its ID. The business must belong to the current account.
    """
    try:
        return delete_business(business_id, current_account.id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting event: {str(e)}")
