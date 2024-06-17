## Blog Api using django Rest framework

### project requirements 

1. Django
2. djangorestframework
3. djangorestframework-simplejwt


###  Api Endpoints

*User Register/Signup (POST)*

```

http://127.0.0.1:8000/v1/api/register/

```


*User Login (POST)*

```

http://127.0.0.1:8000/v1/api/login/

```


*Create Blog by logged in Only (POST)*

(require (key: Authorization and Value: Bearer(access tokenon Headers which can be copied by login as user)

```

http://127.0.0.1:8000/v1/home/blog/

```


*Read Blog for All (GET)*

```

http://127.0.0.1:8000/v1/home/

```


*Edit Blog by Author Only (PATCH)*

```

http://127.0.0.1:8000/v1/home/Blog/

```
(require (key: Authorization and Value: Bearer(access tokenon *Headers* which can be copied by login as user)

( uid )

*Delete Blog by Author Only (DELETE)*

```

http://127.0.0.1:8000/v1/home/Blog/

```
(require (key: Authorization and Value: Bearer(access tokenon *Headers* which can be copied by login as user)

( uid )


