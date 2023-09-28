from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    user_id : str
    account : str
    full_name : str
    email : str
    shipping_address : str
    contact_phone : str