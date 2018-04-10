def Headers2Dict(headers_str):
    
    if not headers_str:
        return {}

    headers = {}
    
    item_list = headers_str.splitlines(keepends=False)
    for item in item_list:
        item_str = item.strip()
        if not item_str:
            continue
        if item_str.startswith(':'):
            continue
        key_value_pair = item_str.split(':')
        if len(key_value_pair) < 2:
            continue
        k, v = key_value_pair[0], key_value_pair[1]
        headers[k] = v.strip()
    return headers


if __name__ == '__main__':
    from pprint import pprint
    
    headers_str = '''
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    Accept-Encoding: gzip, deflate, br
    Accept-Language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7
    Cache-Control: max-age=0
    Connection: keep-alive
    Cookie: QiHooGUID=A839447ABBF0478158F7BB87D88FCE9E.1523279578814; __guid=15484592.2226788641830713000.1523279576870.7004; dpr=1; webp=1; __huid=11kPNvr7a2J37K%2BgKEy5v2SYMa7MP3%2FQRiVFzpi0BQovA%3D; WZWS4=0d3f9c49e9ed6bb33ac543bc1a36352b; __DC_gid=9114931.871246465.1523281715646.1523287353495.34; __gid=9114931.871246465.1523281715646.1523287449349.39; erules=p2-1%7Cp1-19%7Cecr-5%7Cp4-12; _S=a2bgn3j82qf73a11cubsqn83b1; count=53; stc_ls_sohome=Rcz~2OYRKT!QTRX(hWWa; gtHuid=1
    DNT: 1
    Host: www.so.com
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
    '''
    
    headers = Headers2Dict(headers_str)
    pprint(headers)
