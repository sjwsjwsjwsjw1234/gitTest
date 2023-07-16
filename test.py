def fun():
    data=123
    if (1 is 1):
        return data
print(fun())

tmpl_dict = {}
temp_json = ""
code, tmpl_data = utils.http_request(policy_url, "GET")
if code != Errors.success:
    utils.kwai_log(
        sys_tag=self.__tag,
        msg="get tmpl from rhllor fail %s, url: %s, msg: %s"
        % (code, policy_url, tmpl_data),
    )
    return tmpl_json