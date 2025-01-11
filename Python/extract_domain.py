def domain_name(url):
    url = url.replace("http://", "").replace("https://", "")
    
    url = url.lstrip("www.")

    domain_parts = url.split("/")[0].split(".")

    return domain_parts[0]  

