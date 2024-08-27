# Plagapp


```bash
git clone <repo>
```

## Iniciar el proyecto
```bash
docker compose up --build -d
```

## Routes
```
app
  /auth
    /login
    /register
    /logout
```

## Set an admin user

1. Create a new user
2. ```docker exec -it <container id> bash```
3. ```psql -U root plagapp-db```
4. ```UPDATE "user" SET role = 'ADMIN' WHERE email = 'admin@gmail.com';```
