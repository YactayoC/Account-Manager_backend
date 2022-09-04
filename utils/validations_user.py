from validator import validate

ruleRegister = {
    "fullname": "required|min:3",
    "email": "required|mail",
    "password": "required|min:6",
}

ruleLogin = {
    "email": "required|mail",
}


def isEmailValid(email: str):
    result, validated_data, _ = validate({"email": email}, ruleLogin, return_info=True)
    return result


def areValidFields(user: dict):
    result, validated_data, _ = validate(user, ruleRegister, return_info=True)
    return not result
