def application(envion,start_response):
    start_response('200 ok',[('Content-Type','text/html')])
    body='<h1>hello,%s!</h1>'%(envion['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]
