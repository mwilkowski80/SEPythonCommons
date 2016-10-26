
def require_non_None(obj, msg=None,msg_supplier=None):
    """Ensures that obj does not exist or raises TypeError
    Message is either msg or provided by msg_supplier"""
    if not obj:
        raise TypeError(msg or msg_supplier())