import concurrent
from concurrent.futures import ThreadPoolExecutor

def kare(x):
    return x*x
with ThreadPoolExecutor() as uygulayici:
    sonuclar=[]
    for k in range(10):
        sonuclar.append(uygulayici.submit(kare,k))
for f in concurrent.futures.as_completed(sonuclar):
    print(f.result())
