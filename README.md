# Kindler
Python script for on-demand pushing from Pocket to Kindle.

Forked from [sunetos/kindler](https://github.com/sunetos/kindler).

Just leave it running in your PC 24h a day...

## Notes

I had to install before:
```
pip install pyyaml
pip install setproctitle
pip install requests
pip install pyquery
pip install humanize
pip install gevent
```

Get it to work having an http server running:
```
python -m SimpleHTTPServer
```

My cfg.yml:
```
api:
  consumer: ########
  redirect: http://localhost:8000/

users:
- pocket:
    user: ########
    pass: ########
  kindle:
    email: ########@kindle.com

smtp:
  host: smtp.gmail.com
  port: 587
  user: ########@gmail.com
  pass: <Application password! Not your GMAIL!!>
```
