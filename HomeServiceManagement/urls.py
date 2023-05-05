from django.contrib import admin
from django.urls import path
from home_service.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name="home"),
    path('user_home',User_home,name="user_home"),
    path('admin_home/',Admin_Home,name="admin_home"),
    path('service_home',Service_home,name="service_home"),
    path('service',All_Service,name="service"),
    path('profile',profile,name="profile"),
    path('service_profile',service_profile,name="service_profile"),
    path('admin_profile',admin_profile,name="admin_profile"),
    path('edit_profile',Edit_Profile,name="edit_profile"),
    path('edit_service_profile',Edit_Service_Profile,name="edit_service_profile"),
    path('edit_admin_profile',Edit_Admin_Profile,name="edit_admin_profile"),
    path('contact',contact,name="contact"),
    path('about',about,name="about"),
    path('login',Login_User,name="login"),
    path('admin_login',Login_admin,name="admin_login"),
    path('logout',Logout,name="logout"),
    path('signup',Signup_User,name="signup"),
    path('change_password',Change_Password,name="change_password"),
    path('admin_change_password',Admin_Change_Password,name="admin_change_password"),
    path('new_service_man',New_Service_man,name="new_service_man"),
    path('all_service_man',All_Service_man,name="all_service_man"),
    path('all_customer',All_Customer,name="all_customer"),
    path('add_service',Add_Service,name="add_service"),
    path('add_city',Add_City,name="add_city"),
    path('view_service',View_Service,name="view_service"),
    path('view_city',View_City,name="view_city"),
    path('service_order',Service_Order,name="service_order"),
    path('customer_order',Customer_Order,name="customer_order"),
    path('admin_order',Admin_Order,name="admin_order"),
    path('search_report',Search_Report,name="search_report"),
    path('new_message',new_message,name="new_message"),
    path('read_message',read_message,name="read_message"),
    path('search_cities',search_cities,name="search_cities"),
    path('search_services',search_services,name="search_services"),
    path('confirm_message(<int:pid>)',confirm_message,name="confirm_message"),
    path('status(<int:pid>)',Change_status,name="status"),
    path('edit_service(<int:pid>)',Edit_Service,name="edit_service"),
    path('delete_service(<int:pid>)',delete_service,name="delete_service"),
    path('delete_customer(<int:pid>)',delete_customer,name="delete_customer"),
    path('explore_services(<int:pid>)',Explore_Service,name="explore_services"),
    path('booking(<int:pid>)',Customer_Booking,name="booking"),
    path('delete_service_man(<int:pid>)',delete_service_man,name="delete_service_man"),
    path('delete_Booking(<int:pid>)',delete_Booking,name="delete_Booking"),
    path('accept_confirmation(<int:pid>)',accept_confirmation,name="accept_confirmation"),
    path('Booking_detail(<int:pid>)',Booking_detail,name="Booking_detail"),
    path('delete_admin_order(<int:pid>)',delete_admin_order,name="delete_admin_order"),
    path('order_status(<int:pid>)',Order_status,name="order_status"),
    path('order_detail(<int:pid>)',Order_detail,name="order_detail"),
    path('service_man_detail(<int:pid>)',service_man_detail,name="service_man_detail"),
    path('delete_city(<int:pid>)',delete_city,name="delete_city"),
    path('servicemandash',Servicemandash,name="servicemandash"),
    path('cities',Cities,name="cities"),
    path('customersdash',Customersdash,name="customersdash"),
    path('service_dash',Service_dash,name="service_dash"),
    path('citydash',Citydash,name="citydash"),
    path('book_fuel',Book_fuel,name="book_fuel"),
    path('select_fuel_cities',Select_fuel_cities,name="select_fuel_cities"),
    path('fuel_home',Fuel_home,name="fuel_home"),
    path('fuelmandash',Fuelmandash,name="fuelmandash"),
    path('admin_order_dash',Admin_order_dash,name="admin_order_dash"),
    path('fuelman_login',Fuelman_login,name="fuelman_login"),
    path('spares',Spares,name="spares"),
    path('collectionsview(<str:slug>)',Collectionsview,name="collectionsview"),
    path('productview(<str:name>)',Productview,name="productview"),
    path('product/<str:p_slug>/<str:p1_name>/<str:pr_slug>',product,name="product"),
    path('fuel_service_order',Fuel_service_order,name="fuel_service_order"),
    path('fuel_service_profile',Fuel_service_profile,name="fuel_service_profile"),
    path('fuel_edit_service_profile',Fuel_edit_service_profile,name="fuel_edit_service_profile"),
    path('fuel_search_cities',Fuel_search_cities,name="fuel_search_cities"),
    path('fuel_booking(<int:pid>)',Fuel_booking,name="fuel_booking"),
    path('fuel_customer_order',Fuel_customer_order,name="fuel_customer_order"),
    path('fuel_new_service_man',Fuel_new_service_man,name="fuel_new_service_man"),
    path('fuel_all_service_man',Fuel_all_service_man,name="fuel_all_service_man"),
    path('fuel_accept_confirmation(<int:pid>)',fuel_accept_confirmation,name="fuel_accept_confirmation"),
    path('fuel_status(<int:pid>)',Fuel_Change_status,name="fuel_status"),
    path('fuel_service_man_detail(<int:pid>)',fuel_service_man_detail,name="fuel_service_man_detail"),
    path('fuel_delete_service_man(<int:pid>)',fuel_delete_service_man,name="fuel_delete_service_man"),
    path('fuel_admin_order',fuel_admin_order,name="fuel_admin_order"),
    path('fuel_booking_detail(<int:pid>)',fuel_booking_detail,name="fuel_booking_detail"),
    path('fuel_delete_booking(<int:pid>)',fuel_delete_booking,name="fuel_delete_booking"),
    path('fuel_order_status(<int:pid>)',fuel_Order_status,name="fuel_order_status"),
    path('fuel_delete_admin_order(<int:pid>)',fuel_delete_admin_order,name="fuel_delete_admin_order"),
    path('fuel_profile',fuel_profile,name="fuel_profile"),
    path('fuel_change_password',fuel_Change_Password,name="fuel_change_password"),
    path('select_car/<str:name>/',select_car,name="select_car"),
    path('get_carmodels/',get_carmodels,name="get_carmodels"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

