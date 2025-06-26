# 🛍️ E-commerce API - Django REST Framework

A simple RESTful API for an E-commerce backend built with Django and Django REST Framework.

## ✅ Features Implemented

- Custom User Model with Token Authentication
- Email Verification and Password Reset
- User Login, Registration, and Profile View
- Category & Product Management (Create, List, Filter, Search)
- Pagination Support
- Ready for Stripe Payment Integration (Base Setup Done)



## 🚀 Setup Instructions


1. **Clone the repository:**

```bash
git clone https://github.com/siamCSEJnU/django-ecommerce-backend.git
cd django-ecommerce-backend
 ```

2. **Install required packages:**

```bash
pip install django djangorestframework
pip install stripe
pip install django-filter
 ```


3. **Configurations:** 
Create a .env file with these variables:

Get Stripe API keys from Stripe Dashboard

Add to .env:
```bash
STRIPE_SECRET_KEY = your_own_secret_key
STRIPE_PUBLISHABLE_KEY = your_own_publishable_key
 ```
4. **Key Parts**
Don't set authorization header like this

```bash
Authorization: Bearer <your_token>

 ```
 Use like this
```bash
Authorization: Token <your_token>

 ```

5. **Apply Migrations:**

```bash
python manage.py makemigrations
python manage.py migrate

 ```
6. **Run The Server:**

```bash
python manage.py runserver
 ```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Contact
siamahmed234@gmail.com


    
