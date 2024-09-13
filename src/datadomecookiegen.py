import random
import json
import time
import datetime
import urllib.parse
from genmousemovements import generate_mouse_movements

def generate_random_string():
    return f"{random.randint(5, 20)}.{random.randint(1000000000000, 9999999999999)}"

ttst = str(f"{random.randint(5, 18)}.{random.randint(100000000000000, 999999999999999)}")
ttst2 = str(f"{random.randint(5, 18)}.{random.randint(100000000000000, 999999999999999)}")
tagpu = str(f"{random.randint(0, 2)}.{random.randint(1000000000000, 9999999999999)}")
tagpu2 = str(f"{random.randint(0, 2)}.{random.randint(1000000000000, 9999999999999)}")

async def datadome_cookie_ch(proxy, session):
    url = "https://dd.pokemoncenter.com/js/"
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/x-www-form-urlencoded",
        "Dnt": "1",
        "origin": "https://www.pokemoncenter.com",
        "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    jsData = {
        "log1": False,
        "opts": "ajaxListenerPath,endpoint",
        "ttst": ttst,
        "ifov": False,
        "hc": 16,
        "br_oh": 1032,
        "br_ow": 1920,
        "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "wbd": False,
        "dp0": True,
        "tagpu": tagpu,
        "wdif": False,
        "wdifrm": False,
        "npmtm": False,
        "br_h": 1050,
        "br_w": 1400,
        "nddc": 0,
        "rs_h": 1080,
        "rs_w": 1920,
        "rs_cd": 24,
        "phe": False,
        "nm": False,
        "jsf": False,
        "lg": "en-US",
        "pr": 1,
        "ars_h": 1032,
        "ars_w": 1920,
        "tz": 300,
        "str_ss": True,
        "str_ls": True,
        "str_idb": True,
        "str_odb": False,
        "plgod": False,
        "plg": 5,
        "plgne": True,
        "plgre": True,
        "plgof": False,
        "plggt": False,
        "pltod": False,
        "hcovdr": False,
        "hcovdr2": False,
        "plovdr": False,
        "plovdr2": False,
        "ftsovdr": False,
        "ftsovdr2": False,
        "lb": False,
        "eva": 33,
        "lo": False,
        "ts_mtp": 0,
        "ts_tec": False,
        "ts_tsa": False,
        "vnd": "Google Inc.",
        "bid": "NA",
        "mmt": "application/pdf,text/pdf",
        "plu": "PDF Viewer,Chrome PDF Viewer,Chromium PDF Viewer,Microsoft Edge PDF Viewer,WebKit built-in PDF",
        "hdn": False,
        "awe": False,
        "geb": False,
        "dat": False,
        "med": "defined",
        "aco": "probably",
        "acots": False,
        "acmp": "probably",
        "acmpts": True,
        "acw": "probably",
        "acwts": False,
        "acma": "maybe",
        "acmats": False,
        "acaa": "probably",
        "acaats": True,
        "ac3": "",
        "ac3ts": False,
        "acf": "probably",
        "acfts": False,
        "acmp4": "maybe",
        "acmp4ts": False,
        "acmp3": "probably",
        "acmp3ts": False,
        "acwm": "maybe",
        "acwmts": False,
        "ocpt": False,
        "vco": "",
        "vcots": False,
        "vch": "probably",
        "vchts": True,
        "vcw": "probably",
        "vcwts": True,
        "vc3": "maybe",
        "vc3ts": False,
        "vcmp": "",
        "vcmpts": False,
        "vcq": "",
        "vcqts": False,
        "vc1": "probably",
        "vc1ts": True,
        "dvm": 8,
        "sqt": False,
        "so": "landscape-primary",
        "wdw": True,
        "cokys": "bG9hZFRpbWVzY3NpYXBwL=",
        "ecpc": False,
        "lgs": True,
        "lgsod": False,
        "psn": True,
        "edp": True,
        "addt": True,
        "wsdc": True,
        "ccsr": True,
        "nuad": True,
        "bcda": False,
        "idn": True,
        "capi": False,
        "svde": False,
        "vpbq": True,
        "ucdv": False,
        "spwn": False,
        "emt": False,
        "bfr": False,
        "dbov": False,
        "cfpfe": "ZnVuY3Rpb24oKXt2YXIgdD1kb2N1bWVudFsnXHg3MVx4NzVceDY1XHg3Mlx4NzlceDUzXHg2NVx4NmNceDY1XHg2M1x4NzRceDZmXHg3MiddKCdceDYyXHg3Mlx4NmZceDc3XHg3M1x4NjVceDcyXHg2Nlx4NmNceDZmXHg3N1x4MmRceDYzXHg2Zlx4NmVceDc0XHg2",
        "stcfp": "Oi8vZGQucG9rZW1vbmNlbnRlci5jb20vdGFncy5qczoyOjg3NDk3KQogICAgYXQgaHR0cHM6Ly9kZC5wb2tlbW9uY2VudGVyLmNvbS90YWdzLmpzOjI6NTE1MzUKICAgIGF0IG5yV3JhcHBlciAoaHR0cHM6Ly93d3cucG9rZW1vbmNlbnRlci5jb20vOjI6MTg2NTQp",
        "ckwa": True,
        "prm": True,
        "tzp": "America/New_York",
        "cvs": True,
        "usb": "defined",
        "glvd": "Google Inc. (Intel)",
        "glrd": "ANGLE (Intel, Intel(R) Arc(TM) A770 Graphics (0x000056A0) Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "wwl": False,
        "jset": int(time.mktime(datetime.datetime.now().timetuple()))
    }
    data = {
        'jsData': json.dumps(jsData),
        'eventCounters': [],
        'jsType': 'ch',
        'cid': None,
        'ddk': '5B45875B653A484CC79E57036CE9FC',
        'Referer': 'https%3A%2F%2Fwww.pokemoncenter.com%2F',
        'request': '%2F',
        'responsePage': 'origin',
        'ddv': '4.19.2'
    }
    datadome_cookie_value = next((c.value for c in session.cookies if c.name.lower() == 'datadome'), None)

    if datadome_cookie_value:
        data['cid'] = datadome_cookie_value
    else:
        print("ERR session invalid")
    form_data = urllib.parse.urlencode(data)

    print(data)
    response = await session.post(url, headers=headers, json=form_data, proxy=proxy)
    print(response.text)
    try:
        cookie_string = response.text.split('"cookie":"')[1].split('";')[0]
        cookie_parts = cookie_string.split('; ')
        for part in cookie_parts:
            if '=' in part:
                name, value = part.split('=', 1)
                name = name.strip()
                if name.lower() == 'datadome':
                    if 'datadome' in session.cookies:
                        del session.cookies['datadome']

                    session.cookies.set(name, value, domain='.pokemoncenter.com', path='/')
                    print(f"datadome cookie updated/set for ch: {name}={value}")
                    break

    except Exception as e:
        print(f"Error parsing for cookie: {e}")

    print("Cookies after ch gen attempt:", session.cookies)

    return session

async def datadome_cookie_le(proxy, session):

    url = "https://dd.pokemoncenter.com/js/"
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/x-www-form-urlencoded",
        "Dnt": "1",
        "origin": "https://www.pokemoncenter.com",
        "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    random_data = generate_mouse_movements()

    jsData = {
        "log1": False,
        "opts": "ajaxListenerPath,endpoint",
        "ttst": ttst,
        "mp_cx": 568,
        "mp_cy": 472,
        "mp_tr": True,
        "mp_mx": 9,
        "mp_my": 5,
        "mp_sx": 568,
        "mp_sy": 559,
        "mm_md": 115,
        "ifov": False,
        "hc": 16,
        "br_oh": 1032,
        "br_ow": 1920,
        "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "wbd": False,
        "dp0": True,
        "tagpu": tagpu,
        "wdif": False,
        "wdifrm": False,
        "npmtm": False,
        "br_h": 1050,
        "br_w": 1400,
        "nddc": 1,
        "rs_h": 1080,
        "rs_w": 1920,
        "rs_cd": 24,
        "phe": False,
        "nm": False,
        "jsf": False,
        "lg": "en-US",
        "pr": 1,
        "ars_h": 1032,
        "ars_w": 1920,
        "tz": 300,
        "str_ss": True,
        "str_ls": True,
        "str_idb": True,
        "str_odb": False,
        "plgod": False,
        "plg": 5,
        "plgne": True,
        "plgre": True,
        "plgof": False,
        "plggt": False,
        "pltod": False,
        "hcovdr": False,
        "hcovdr2": False,
        "plovdr": False,
        "plovdr2": False,
        "ftsovdr": False,
        "ftsovdr2": False,
        "lb": False,
        "eva": 33,
        "lo": False,
        "ts_mtp": 0,
        "ts_tec": False,
        "ts_tsa": False,
        "vnd": "Google Inc.",
        "bid": "NA",
        "mmt": "application/pdf,text/pdf",
        "plu": "PDF Viewer,Chrome PDF Viewer,Chromium PDF Viewer,Microsoft Edge PDF Viewer,WebKit built-in PDF",
        "hdn": False,
        "awe": False,
        "geb": False,
        "dat": False,
        "med": "defined",
        "aco": "probably",
        "acots": False,
        "acmp": "probably",
        "acmpts": True,
        "acw": "probably",
        "acwts": False,
        "acma": "maybe",
        "acmats": False,
        "acaa": "probably",
        "acaats": True,
        "ac3": "",
        "ac3ts": False,
        "acf": "probably",
        "acfts": False,
        "acmp4": "maybe",
        "acmp4ts": False,
        "acmp3": "probably",
        "acmp3ts": False,
        "acwm": "maybe",
        "acwmts": False,
        "ocpt": False,
        "vco": "",
        "vcots": False,
        "vch": "probably",
        "vchts": True,
        "vcw": "probably",
        "vcwts": True,
        "vc3": "maybe",
        "vc3ts": False,
        "vcmp": "",
        "vcmpts": False,
        "vcq": "",
        "vcqts": False,
        "vc1": "probably",
        "vc1ts": True,
        "dvm": 8,
        "sqt": False,
        "so": "landscape-primary",
        "wdw": True,
        "cokys": "bG9hZFRpbWVzY3NpYXBwL=",
        "ecpc": False,
        "lgs": True,
        "lgsod": False,
        "psn": True,
        "edp": True,
        "addt": True,
        "wsdc": True,
        "ccsr": True,
        "nuad": True,
        "bcda": False,
        "idn": True,
        "capi": False,
        "svde": False,
        "vpbq": True,
        "ucdv": False,
        "spwn": False,
        "emt": False,
        "bfr": False,
        "dbov": False,
        "cfpfe": "ZnVuY3Rpb24oKXt2YXIgdD1kb2N1bWVudFsnXHg3MVx4NzVceDY1XHg3Mlx4NzlceDUzXHg2NVx4NmNceDY1XHg2M1x4NzRceDZmXHg3MiddKCdceDYyXHg3Mlx4NmZceDc3XHg3M1x4NjVceDcyXHg2Nlx4NmNceDZmXHg3N1x4MmRceDYzXHg2Zlx4NmVceDc0XHg2",
        "stcfp": "Oi8vZGQucG9rZW1vbmNlbnRlci5jb20vdGFncy5qczoyOjg3NDk3KQogICAgYXQgaHR0cHM6Ly9kZC5wb2tlbW9uY2VudGVyLmNvbS90YWdzLmpzOjI6NTE1MzUKICAgIGF0IG5yV3JhcHBlciAoaHR0cHM6Ly93d3cucG9rZW1vbmNlbnRlci5jb20vOjI6MTg2NTQp",
        "ckwa": True,
        "prm": True,
        "tzp": "America/New_York",
        "cvs": True,
        "usb": "defined",
        "glvd": "Google Inc. (Intel)",
        "glrd": "ANGLE (Intel, Intel(R) Arc(TM) A770 Graphics (0x000056A0) Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "wwl": False,
        "jset": int(time.mktime(datetime.datetime.now().timetuple())),
        "dcok": ".pokemoncenter.com",
        "log2": True,
        "es_sigmdn": 0.06111527681106614,
        "es_mumdn": 8.06412297519166,
        "es_distmdn": 270.06650801107634,
        "es_angsmdn": 2.427143017494427,
        "es_angemdn": 2.787279517525958,
        "m_s_c": 0,
        "m_m_c": 607,
        "m_c_c": 0,
        "m_cm_r": 0,
        "m_ms_r": -1
    }
    jsData.update({
        "mp_cx": random_data["mp_cx"],
        "mp_cy": random_data["mp_cy"],
        "mp_tr": random_data.get("mp_tr", True),
        "mp_mx": random_data.get("mp_mx", 0),
        "mp_my": random_data.get("mp_my", 0),
        "mp_sx": random_data.get("mp_sx", 0),
        "mp_sy": random_data.get("mp_sy", 0),
        "mm_md": random_data["mm_md"],
        "es_sigmdn": random_data["es_sigmdn"],
        "es_mumdn": random_data["es_mumdn"],
        "es_distmdn": random_data["es_distmdn"],
        "es_angsmdn": random_data["es_angsmdn"],
        "es_angemdn": random_data["es_angemdn"],
        "m_s_c": random_data["m_s_c"],
        "m_m_c": random_data["m_m_c"],
        "m_c_c": random_data["m_c_c"],
        "m_cm_r": random_data["m_cm_r"],
        "m_ms_r": random_data["m_ms_r"]
    })
    event_counters = {
        "mousemove": random_data["m_m_c"],
        "click": random_data["m_c_c"],
        "scroll": random_data["m_s_c"],
        "touchstart": 0,
        "touchend": 0,
        "touchmove": 0,
        "keydown": 0,
        "keyup": 0
    }
    data = {
        'jsData': json.dumps(jsData),
        'eventCounters': json.dumps(event_counters),
        'jsType': 'le',
        'cid': None,
        'ddk': '5B45875B653A484CC79E57036CE9FC',
        'Referer': 'https%3A%2F%2Fwww.pokemoncenter.com%2F',
        'request': '%2F',
        'responsePage': 'origin',
        'ddv': '4.19.2'
    }
    datadome_cookie_value = next((c.value for c in session.cookies if c.name.lower() == 'datadome'), None)

    if datadome_cookie_value:
        data['cid'] = datadome_cookie_value
    else:
        print("Datadome cookie not found in the session.")

    form_data = urllib.parse.urlencode(data)
    response = await session.post(url, headers=headers, json=form_data, proxy=proxy)
    print(response.text)
    try:
        cookie_string = response.text.split('"cookie":"')[1].split('";')[0]
        cookie_parts = cookie_string.split('; ')
        for part in cookie_parts:
            if '=' in part:
                name, value = part.split('=', 1)
                name = name.strip()
                if name.lower() == 'datadome':
                    if 'datadome' in session.cookies:
                        del session.cookies['datadome']

                    session.cookies.set(name, value, domain='.pokemoncenter.com', path='/')
                    print(f"datadome cookie updated/set for le: {name}={value}")
                    break

    except Exception as e:
        print(f"Error parsing for cookie: {e}")

    print("Cookies after attempting to set le cookie:", session.cookies)
    return session

