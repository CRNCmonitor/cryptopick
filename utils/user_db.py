import json`nFILE="users.json"`ndef load_users():`n    try: return json.load(open(FILE))`n    except: return {}`ndef save_users(db): json.dump(db,open(FILE,"w"))
