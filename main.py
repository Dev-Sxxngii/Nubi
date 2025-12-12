import manager.manager as manager

def main(site, text, page):
    try:
        return manager.manager(site, text, page) 
    except Exception as e:
        print(f"[ERROR] 크롤링 실패: {e}")
        return None