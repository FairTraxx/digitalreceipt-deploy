Good morning everyone, The API has been written, tested and deployed on heroku. It's currently up and running on Postgres for it's database, You can fully use it now, If you need access to the admin panel DM me.

Start here --> https://gentle-dusk-67310.herokuapp.com/auth/users/ (Register the User first)

Log the user in and assign token--->https://gentle-dusk-67310.herokuapp.com/auth/token/login/ (with login credientals created while registering)

Log the user out and destroy token--->https://gentle-dusk-67310.herokuapp.com/auth/token/logout/ (logout with same credientals)

More endpoints: (ready to be tested/used though some features might need some more tinkering around)

https://gentle-dusk-67310.herokuapp.com/auth/users/activation/ (sends an activation email) (requires more work)

https://gentle-dusk-67310.herokuapp.com/auth/users/resend_activation/ (Resends activation email) (requires more work)

https://gentle-dusk-67310.herokuapp.com/auth/users/me/  (Deletes an account)(works)

https://gentle-dusk-67310.herokuapp.com/auth/users/set_{USERNAME_FIELD}/ (Changes username) (works)

https://gentle-dusk-67310.herokuapp.com/auth/users/reset_{USERNAME_FIELD}/ (sends an email to change username) (requires more work)

https://gentle-dusk-67310.herokuapp.com/auth/users/set_password/  (change password) (works ?)

https://gentle-dusk-67310.herokuapp.com/auth/users/reset_password/ (sends a password change email) (requires more...)

---Additional testing and DB access
https://gentle-dusk-67310.herokuapp.com/admin (DM for superuser)
