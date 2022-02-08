import json
import sys

import pymysql
import requests
from bs4 import BeautifulSoup as BS
import datetime


# res = requests.get("https://www.electroplanet.ma/smartphone-tablette-gps/smartphone/iphone?product_list_limit=60")
# html = res.text



# items = BS(
#     html ,
#     features="html.parser"
# )

# list_items = items.find('ol' , {'class' , 'products list items product-items row'})

list_items= """
<ol class="products list items product-items row">
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <div class="remise-cac">
   <h3 class="title-cac-product">
    Bon de remise de
    <span>
     379
     <span class="currency">
      DH
     </span>
    </span>
   </h3>
  </div>
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/pcac2828080-cac-iphone-12-pro-max-256gb-pacific-blue-mgdf3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="CAC IPHONE 12 PRO MAX 256GB PACIFIC BLUE  MGDF3AA/A+ECOUTEURS FIL LIGHTNING EARPODS MMTN2ZM/A APPLE" class="product-image-photo" height="" src="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/2/8/2828080-2832636.jpg" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15420,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/pcac2828080-cac-iphone-12-pro-max-256gb-pacific-blue-mgdf3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        ECOUTEURS LIGHTNING EA...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15420" data-product-id="15420" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -2%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          17 378
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          16 999
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/pcac2828080-cac-iphone-12-pro-max-256gb-pacific-blue-mgdf3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15420,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15420","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_30" title="En stock">
        En stock
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <div class="remise-cac">
   <h3 class="title-cac-product">
    Bon de remise de
    <span>
     379
     <span class="currency">
      DH
     </span>
    </span>
   </h3>
  </div>
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/pcac2828079-cac-iphone-12-pro-max-256gb-graphite-mgdc3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="CAC IPHONE 12 PRO MAX 256GB GRAPHITE  MGDC3AA/A+ECOUTEURS FIL LIGHTNING EARPODS MMTN2ZM/A APPLE" class="product-image-photo" height="" src="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/2/8/2828079-2832636.jpg" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15419,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/pcac2828079-cac-iphone-12-pro-max-256gb-graphite-mgdc3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        ECOUTEURS LIGHTNING EA...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15419" data-product-id="15419" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -2%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          17 378
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          16 999
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/pcac2828079-cac-iphone-12-pro-max-256gb-graphite-mgdc3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15419,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15419","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_30" title="En stock">
        En stock
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <div class="remise-cac">
   <h3 class="title-cac-product">
    Bon de remise de
    <span>
     379
     <span class="currency">
      DH
     </span>
    </span>
   </h3>
  </div>
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/pcac2828073-cac-iphone-12-pro-max-128gb-graphite-mgd73aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="CAC IPHONE 12 PRO MAX 128GB GRAPHITE  MGD73AA/A+ECOUTEURS FIL LIGHTNING EARPODS MMTN2ZM/A APPLE" class="product-image-photo" height="" src="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/2/8/2828073-2832636.jpg" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15404,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/pcac2828073-cac-iphone-12-pro-max-128gb-graphite-mgd73aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        ECOUTEURS LIGHTNING EA...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15404" data-product-id="15404" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -2%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          14 378
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          13 999
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/pcac2828073-cac-iphone-12-pro-max-128gb-graphite-mgd73aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15404,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15404","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_30" title="En stock">
        En stock
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <div class="remise-cac">
   <h3 class="title-cac-product">
    Bon de remise de
    <span>
     379
     <span class="currency">
      DH
     </span>
    </span>
   </h3>
  </div>
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/pcac2828061-cac-iphone-12-pro-128gb-silver-mgml3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="CAC IPHONE 12 PRO 128GB SILVER  MGML3AA/A+ECOUTEURS FIL LIGHTNING EARPODS MMTN2ZM/A APPLE" class="product-image-photo" height="" src="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/2/8/2828061-2832636.jpg" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15403,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/pcac2828061-cac-iphone-12-pro-128gb-silver-mgml3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        ECOUTEURS LIGHTNING EA...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15403" data-product-id="15403" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -2%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          14 678
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          14 299
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/pcac2828061-cac-iphone-12-pro-128gb-silver-mgml3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15403,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15403","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_30" title="En stock">
        En stock
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <div class="remise-cac">
   <h3 class="title-cac-product">
    Bon de remise de
    <span>
     379
     <span class="currency">
      DH
     </span>
    </span>
   </h3>
  </div>
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/pcac2828033-cac-iphone-12-64gb-black-mgj53aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="CAC IPHONE 12 64GB BLACK  MGJ53AA/A+ECOUTEURS FIL LIGHTNING EARPODS MMTN2ZM/A APPLE" class="product-image-photo" height="" src="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/2/8/2828033-2832636.jpg" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15398,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/pcac2828033-cac-iphone-12-64gb-black-mgj53aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        ECOUTEURS LIGHTNING EA...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15398" data-product-id="15398" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -3%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          10 069
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          9 690
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/pcac2828033-cac-iphone-12-64gb-black-mgj53aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15398,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15398","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_30" title="En stock">
        En stock
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <div class="remise-cac">
   <h3 class="title-cac-product">
    Bon de remise de
    <span>
     379
     <span class="currency">
      DH
     </span>
    </span>
   </h3>
  </div>
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/pcac2827999-cac-iphone-11-128gb-black-mhdh3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="CAC IPHONE 11 128GB BLACK  MHDH3AA/A+ECOUTEURS FIL LIGHTNING EARPODS MMTN2ZM/A APPLE" class="product-image-photo" height="" src="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/2/8/2827999-2832636.jpg" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15397,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/pcac2827999-cac-iphone-11-128gb-black-mhdh3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        ECOUTEURS LIGHTNING EA...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15397" data-product-id="15397" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -4%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          8 278
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          7 899
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/pcac2827999-cac-iphone-11-128gb-black-mhdh3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15397,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15397","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_30" title="En stock">
        En stock
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <div class="remise-cac">
   <h3 class="title-cac-product">
    Bon de remise de
    <span>
     379
     <span class="currency">
      DH
     </span>
    </span>
   </h3>
  </div>
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/pcac2827993-cac-iphone-11-64gb-black-mhda3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="CAC IPHONE 11 64GB BLACK  MHDA3AA/A+ECOUTEURS FIL LIGHTNING EARPODS MMTN2ZM/A APPLE" class="product-image-photo" height="" src="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/2/8/2827993-2832636.jpg" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15396,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/pcac2827993-cac-iphone-11-64gb-black-mhda3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        ECOUTEURS LIGHTNING EA...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15396" data-product-id="15396" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -5%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          7 378
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          6 999
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/pcac2827993-cac-iphone-11-64gb-black-mhda3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15396,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15396","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_30" title="En stock">
        En stock
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p2908646-apple-iphone-13-pro-max-128g-graphite.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="APPLE IPHONE 13 PRO MAX 128G GRAPHITE" class="product-image-photo" height="" src="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/g/r/graphite_3.jpg" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15102,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p2908646-apple-iphone-13-pro-max-128g-graphite.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        IPHONE 13 PRO MAX 128G...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15102" data-product-id="15102" data-role="priceBox">
      <div class="special-price one_price">
       <span class="price-container price-final_price tax weee">
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          15 490
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </div>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p2908646-apple-iphone-13-pro-max-128g-graphite.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15102,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15102","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_30" title="En stock">
        En stock
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p2908647-apple-iphone-13-pro-max-128g-silver.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="APPLE IPHONE 13 PRO MAX 128G SILVER" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/s/i/silver_4.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15100,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p2908647-apple-iphone-13-pro-max-128g-silver.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        IPHONE 13 PRO MAX 128G...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15100" data-product-id="15100" data-role="priceBox">
      <div class="special-price one_price">
       <span class="price-container price-final_price tax weee">
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          15 490
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </div>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p2908647-apple-iphone-13-pro-max-128g-silver.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15100,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15100","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_30" title="En stock">
        En stock
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p2908652-apple-iphone-13-pro-max-256g-gold.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="APPLE IPHONE 13 PRO MAX 256G GOLD" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/g/o/gold.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15098,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p2908652-apple-iphone-13-pro-max-256g-gold.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        IPHONE 13 PRO MAX 256G GOLD
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15098" data-product-id="15098" data-role="priceBox">
      <div class="special-price one_price">
       <span class="price-container price-final_price tax weee">
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          16 990
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </div>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p2908652-apple-iphone-13-pro-max-256g-gold.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15098,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15098","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_30" title="En stock">
        En stock
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p2908657-apple-iphone-13-pro-max-512g-sierra-bleu.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="APPLE IPHONE 13 PRO MAX 512G SIERRA BLEU" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/s/i/sierra_bleu_6.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15093,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p2908657-apple-iphone-13-pro-max-512g-sierra-bleu.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        IPHONE 13 PRO MAX 512G...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15093" data-product-id="15093" data-role="priceBox">
      <div class="special-price one_price">
       <span class="price-container price-final_price tax weee">
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          19 890
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </div>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p2908657-apple-iphone-13-pro-max-512g-sierra-bleu.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15093,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15093","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_30" title="En stock">
        En stock
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p2908600-apple-iphone-13-128go-midnight.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="APPLE IPHONE 13 128GO MIDNIGHT" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/i/p/iphone_13_midnight_pure_back_iphone_13_midnight_pure_front_2-up_screen__usen.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15087,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p2908600-apple-iphone-13-128go-midnight.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        IPHONE 13 128GO MIDNIGHT
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15087" data-product-id="15087" data-role="priceBox">
      <div class="special-price one_price">
       <span class="price-container price-final_price tax weee">
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          11 249
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </div>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p2908600-apple-iphone-13-128go-midnight.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15087,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15087","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_30" title="En stock">
        En stock
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p2908605-apple-iphone-13-256g-midnight.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="APPLE IPHONE 13 256G MIDNIGHT" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/i/p/iphone_13_midnight_pure_back_iphone_13_midnight_pure_front_2-up_screen__usen_1.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15085,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p2908605-apple-iphone-13-256g-midnight.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        IPHONE 13 256G MIDNIGHT
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15085" data-product-id="15085" data-role="priceBox">
      <div class="special-price one_price">
       <span class="price-container price-final_price tax weee">
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          12 790
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </div>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p2908605-apple-iphone-13-256g-midnight.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15085,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15085","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_30" title="En stock">
        En stock
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p2908602-apple-iphone-13-128g-rose.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="APPLE IPHONE 13 128G ROSE" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/i/p/iphone_13_pink_pure_back_iphone_13_pink_pure_front_2-up_screen__usen.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15082,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p2908602-apple-iphone-13-128g-rose.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        IPHONE 13 128G ROSE
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15082" data-product-id="15082" data-role="priceBox">
      <div class="special-price one_price">
       <span class="price-container price-final_price tax weee">
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          11 249
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </div>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p2908602-apple-iphone-13-128g-rose.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15082,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15082","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_30" title="En stock">
        En stock
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p2827993-apple-iphone-11-64-go-noir.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="APPLE IPHONE 11 64 GO NOIR" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/i/p/iphone_11_black_2-up_vertical_us-en_screen.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":14459,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p2827993-apple-iphone-11-64-go-noir.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        IPHONE 11 64 GO NOIR
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-14459" data-product-id="14459" data-role="priceBox">
      <div class="special-price one_price">
       <span class="price-container price-final_price tax weee">
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          6 999
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </div>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p2827993-apple-iphone-11-64-go-noir.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":14459,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"14459","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_30" title="En stock">
        En stock
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p2828080-apple-iphone-12-pro-max-256gb-pacific-blu.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="APPLE IPHONE 12 PRO MAX 256GB PACIFIC BLU" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/1/2/12pro_max.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":14435,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p2828080-apple-iphone-12-pro-max-256gb-pacific-blu.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        IPHONE 12 PRO MAX 256G...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-14435" data-product-id="14435" data-role="priceBox">
      <div class="special-price one_price">
       <span class="price-container price-final_price tax weee">
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          13 999
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </div>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p2828080-apple-iphone-12-pro-max-256gb-pacific-blu.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":14435,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"14435","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_30" title="En stock">
        En stock
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p2828081-apple-iphone-12-pro-max-256gb-silver.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="APPLE IPHONE 12 PRO MAX 256GB SILVER" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/1/2/12pro_max_silver.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":14434,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p2828081-apple-iphone-12-pro-max-256gb-silver.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        IPHONE 12 PRO MAX 256G...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-14434" data-product-id="14434" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -11%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          16 999
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          14 999
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p2828081-apple-iphone-12-pro-max-256gb-silver.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":14434,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"14434","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_30" title="En stock">
        En stock
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p2828079-apple-iphone-12-pro-max-256go-graphite.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="APPLE IPHONE 12 PRO MAX 256GO GRAPHITE" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/1/2/12promax_noir.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":14433,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p2828079-apple-iphone-12-pro-max-256go-graphite.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        IPHONE 12 PRO MAX 256G...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-14433" data-product-id="14433" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -11%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          16 999
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          14 999
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p2828079-apple-iphone-12-pro-max-256go-graphite.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":14433,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"14433","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_30" title="En stock">
        En stock
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p2828073-apple-iphone-12-pro-max-128-go-graphite.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="APPLE IPHONE 12 PRO MAX 128 GO GRAPHITE" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/1/2/12promax_noir_1.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":14430,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p2828073-apple-iphone-12-pro-max-128-go-graphite.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        IPHONE 12 PRO MAX 128 ...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-14430" data-product-id="14430" data-role="priceBox">
      <div class="special-price one_price">
       <span class="price-container price-final_price tax weee">
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          13 999
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </div>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p2828073-apple-iphone-12-pro-max-128-go-graphite.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":14430,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"14430","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_30" title="En stock">
        En stock
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p2828074-apple-iphone-12-pro-max-128gb-pacific-blu.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="APPLE IPHONE 12 PRO MAX 128GB PACIFIC BLU" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/1/2/12pro_max_bleu.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":14429,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p2828074-apple-iphone-12-pro-max-128gb-pacific-blu.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        IPHONE 12 PRO MAX 128G...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-14429" data-product-id="14429" data-role="priceBox">
      <div class="special-price one_price">
       <span class="price-container price-final_price tax weee">
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          15 599
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </div>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p2828074-apple-iphone-12-pro-max-128gb-pacific-blu.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":14429,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"14429","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_30" title="En stock">
        En stock
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p2828035-apple-iphone-12-64go-vert.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="APPLE IPHONE 12 64GO VERT" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/i/p/iphone_12_green_pure_front_iphone_12_green_pure_back_2-up_screen__usen_3.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":14385,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p2828035-apple-iphone-12-64go-vert.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        IPHONE 12 64GO VERT
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-14385" data-product-id="14385" data-role="priceBox">
      <div class="special-price one_price">
       <span class="price-container price-final_price tax weee">
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          9 690
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </div>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p2828035-apple-iphone-12-64go-vert.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":14385,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"14385","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_30" title="En stock">
        En stock
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p2828033-apple-iphone-12-64-go-noir.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="APPLE IPHONE 12 64 GO NOIR" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/i/p/iphone_12_black_pure_front_iphone_12_black_pure_back_2-up_screen__usen_4.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":14383,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p2828033-apple-iphone-12-64-go-noir.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        IPHONE 12 64 GO NOIR
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-14383" data-product-id="14383" data-role="priceBox">
      <div class="special-price one_price">
       <span class="price-container price-final_price tax weee">
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          9 690
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </div>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p2828033-apple-iphone-12-64-go-noir.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":14383,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"14383","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_30" title="En stock">
        En stock
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p2828061-apple-iphone-12-pro-128-go-silver.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="APPLE IPHONE 12 PRO 128 GO SILVER" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/i/p/iphone_12_pro_silver_pure_front_iphone_12_pro_silver_pure_back_2-up_screen__usen_5.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":14330,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p2828061-apple-iphone-12-pro-128-go-silver.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        IPHONE 12 PRO 128 GO SILVER
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-14330" data-product-id="14330" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -9%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          14 299
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          12 999
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p2828061-apple-iphone-12-pro-128-go-silver.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":14330,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"14330","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_30" title="En stock">
        En stock
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p2828059-apple-iphone-12-pro-128-go-graphite.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="APPLE IPHONE 12 PRO 128 GO GRAPHITE" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/i/p/iphone_12_pro_graphite_pure_front_iphone_12_pro_graphite_pure_back_2-up_screen__usen_4.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":14329,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p2828059-apple-iphone-12-pro-128-go-graphite.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        IPHONE 12 PRO 128 GO G...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-14329" data-product-id="14329" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -9%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          14 299
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          12 999
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p2828059-apple-iphone-12-pro-128-go-graphite.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":14329,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"14329","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_30" title="En stock">
        En stock
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p2549620-apple-iphone-se-noir-128-go.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="APPLE IPHONE SE NOIR 128 GO" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/i/p/iphonese_wwen_image_black_1a_1.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":13232,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p2549620-apple-iphone-se-noir-128-go.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        IPHONE SE NOIR 128 GO
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-13232" data-product-id="13232" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -11%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          6 799
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          6 000
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p2549620-apple-iphone-se-noir-128-go.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":13232,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"13232","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_30" title="En stock">
        En stock
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <div class="remise-cac">
   <h3 class="title-cac-product">
    Bon de remise de
    <span>
     379
     <span class="currency">
      DH
     </span>
    </span>
   </h3>
  </div>
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/pcac2908614-cac-iphone-13-mlqg3aa-a-512gb-blue-apple-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="CAC IPHONE 13 MLQG3AA/A 512GB BLUE APPLE+ECOUTEURS FIL LIGHTNING EARPODS MMTN2ZM/A APPLE" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/2/9/2908614-2832636.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15422,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/pcac2908614-cac-iphone-13-mlqg3aa-a-512gb-blue-apple-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        ECOUTEURS LIGHTNING EA...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15422" data-product-id="15422" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -2%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          15 869
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          15 490
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/pcac2908614-cac-iphone-13-mlqg3aa-a-512gb-blue-apple-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15422,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15422","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_1" title="Indisponible">
        Indisponible
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <div class="remise-cac">
   <h3 class="title-cac-product">
    Bon de remise de
    <span>
     379
     <span class="currency">
      DH
     </span>
    </span>
   </h3>
  </div>
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/pcac2828081-cac-iphone-12-pro-max-256gb-silver-mgdd3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="CAC IPHONE 12 PRO MAX 256GB SILVER  MGDD3AA/A+ECOUTEURS FIL LIGHTNING EARPODS MMTN2ZM/A APPLE" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/2/8/2828081-2832636.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15421,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/pcac2828081-cac-iphone-12-pro-max-256gb-silver-mgdd3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        ECOUTEURS LIGHTNING EA...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15421" data-product-id="15421" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -2%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          17 378
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          16 999
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/pcac2828081-cac-iphone-12-pro-max-256gb-silver-mgdd3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15421,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15421","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_1" title="Indisponible">
        Indisponible
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <div class="remise-cac">
   <h3 class="title-cac-product">
    Bon de remise de
    <span>
     379
     <span class="currency">
      DH
     </span>
    </span>
   </h3>
  </div>
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/pcac2828072-cac-iphone-12-pro-max-128gb-gold-mgd93aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="CAC IPHONE 12 PRO MAX 128GB GOLD  MGD93AA/A+ECOUTEURS FIL LIGHTNING EARPODS MMTN2ZM/A APPLE" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/2/8/2828072-2832636.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15418,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/pcac2828072-cac-iphone-12-pro-max-128gb-gold-mgd93aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        ECOUTEURS LIGHTNING EA...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15418" data-product-id="15418" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -2%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          15 078
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          14 699
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/pcac2828072-cac-iphone-12-pro-max-128gb-gold-mgd93aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15418,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15418","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_1" title="Indisponible">
        Indisponible
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <div class="remise-cac">
   <h3 class="title-cac-product">
    Bon de remise de
    <span>
     379
     <span class="currency">
      DH
     </span>
    </span>
   </h3>
  </div>
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/pcac2828040-cac-iphone-12-128gb-green-mgjf3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="CAC IPHONE 12 128GB GREEN  MGJF3AA/A+ECOUTEURS FIL LIGHTNING EARPODS MMTN2ZM/A APPLE" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/2/8/2828040-2832636.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15417,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/pcac2828040-cac-iphone-12-128gb-green-mgjf3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        ECOUTEURS LIGHTNING EA...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15417" data-product-id="15417" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -3%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          10 878
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          10 499
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/pcac2828040-cac-iphone-12-128gb-green-mgjf3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15417,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15417","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_1" title="Indisponible">
        Indisponible
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <div class="remise-cac">
   <h3 class="title-cac-product">
    Bon de remise de
    <span>
     379
     <span class="currency">
      DH
     </span>
    </span>
   </h3>
  </div>
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/pcac2908635-cac-iphone-13-pro-mlvf3aa-a-256gb-silver-apple-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="CAC IPHONE 13 PRO MLVF3AA/A 256GB SILVER APPLE+ECOUTEURS FIL LIGHTNING EARPODS MMTN2ZM/A APPLE" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/2/9/2908635-2832636.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15415,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/pcac2908635-cac-iphone-13-pro-mlvf3aa-a-256gb-silver-apple-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        ECOUTEURS LIGHTNING EA...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15415" data-product-id="15415" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -2%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          16 169
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          15 790
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/pcac2908635-cac-iphone-13-pro-mlvf3aa-a-256gb-silver-apple-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15415,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15415","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_1" title="Indisponible">
        Indisponible
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <div class="remise-cac">
   <h3 class="title-cac-product">
    Bon de remise de
    <span>
     379
     <span class="currency">
      DH
     </span>
    </span>
   </h3>
  </div>
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/pcac2908631-cac-iphone-13-pro-mlva3aa-a-128gb-silver-apple-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="CAC IPHONE 13 PRO MLVA3AA/A 128GB SILVER APPLE+ECOUTEURS FIL LIGHTNING EARPODS MMTN2ZM/A APPLE" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/2/9/2908631-2832636.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15414,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/pcac2908631-cac-iphone-13-pro-mlva3aa-a-128gb-silver-apple-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        ECOUTEURS LIGHTNING EA...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15414" data-product-id="15414" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -2%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          14 669
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          14 290
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/pcac2908631-cac-iphone-13-pro-mlva3aa-a-128gb-silver-apple-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15414,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15414","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_1" title="Indisponible">
        Indisponible
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <div class="remise-cac">
   <h3 class="title-cac-product">
    Bon de remise de
    <span>
     379
     <span class="currency">
      DH
     </span>
    </span>
   </h3>
  </div>
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/pcac2908660-cac-iphone-13-pro-max-mllm3aa-a-1tb-gold-apple-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="CAC IPHONE 13 PRO MAX MLLM3AA/A 1TB GOLD APPLE+ECOUTEURS FIL LIGHTNING EARPODS MMTN2ZM/A APPLE" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/2/9/2908660-2832636.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15413,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/pcac2908660-cac-iphone-13-pro-max-mllm3aa-a-1tb-gold-apple-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        ECOUTEURS LIGHTNING EA...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15413" data-product-id="15413" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -1%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          23 069
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          22 690
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/pcac2908660-cac-iphone-13-pro-max-mllm3aa-a-1tb-gold-apple-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15413,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15413","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_1" title="Indisponible">
        Indisponible
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <div class="remise-cac">
   <h3 class="title-cac-product">
    Bon de remise de
    <span>
     379
     <span class="currency">
      DH
     </span>
    </span>
   </h3>
  </div>
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/pcac2908657-cac-iphone-13-pro-max-mllj3aa-a-512gb-sierrablue-appl-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="CAC IPHONE 13 PRO MAX MLLJ3AA/A 512GB SIERRABLUE APPL+ECOUTEURS FIL LIGHTNING EARPODS MMTN2ZM/A APPLE" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/2/9/2908657-2832636.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15412,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/pcac2908657-cac-iphone-13-pro-max-mllj3aa-a-512gb-sierrablue-appl-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        ECOUTEURS LIGHTNING EA...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15412" data-product-id="15412" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -1%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          20 269
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          19 890
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/pcac2908657-cac-iphone-13-pro-max-mllj3aa-a-512gb-sierrablue-appl-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15412,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15412","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_1" title="Indisponible">
        Indisponible
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <div class="remise-cac">
   <h3 class="title-cac-product">
    Bon de remise de
    <span>
     379
     <span class="currency">
      DH
     </span>
    </span>
   </h3>
  </div>
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/pcac2908650-cac-iphone-13-pro-max-mlla3aa-a-256gb-graphite-apple-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="CAC IPHONE 13 PRO MAX MLLA3AA/A 256GB GRAPHITE APPLE+ECOUTEURS FIL LIGHTNING EARPODS MMTN2ZM/A APPLE" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/2/9/2908650-2832636.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15411,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/pcac2908650-cac-iphone-13-pro-max-mlla3aa-a-256gb-graphite-apple-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        ECOUTEURS LIGHTNING EA...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15411" data-product-id="15411" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -2%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          17 369
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          16 990
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/pcac2908650-cac-iphone-13-pro-max-mlla3aa-a-256gb-graphite-apple-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15411,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15411","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_1" title="Indisponible">
        Indisponible
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <div class="remise-cac">
   <h3 class="title-cac-product">
    Bon de remise de
    <span>
     379
     <span class="currency">
      DH
     </span>
    </span>
   </h3>
  </div>
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/pcac2908646-cac-iphone-13-pro-max-mll63aa-a-128gb-graphite-apple-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="CAC IPHONE 13 PRO MAX MLL63AA/A 128GB GRAPHITE APPLE+ECOUTEURS FIL LIGHTNING EARPODS MMTN2ZM/A APPLE" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/2/9/2908646-2832636.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15410,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/pcac2908646-cac-iphone-13-pro-max-mll63aa-a-128gb-graphite-apple-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        ECOUTEURS LIGHTNING EA...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15410" data-product-id="15410" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -2%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          15 869
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          15 490
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/pcac2908646-cac-iphone-13-pro-max-mll63aa-a-128gb-graphite-apple-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15410,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15410","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_1" title="Indisponible">
        Indisponible
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <div class="remise-cac">
   <h3 class="title-cac-product">
    Bon de remise de
    <span>
     379
     <span class="currency">
      DH
     </span>
    </span>
   </h3>
  </div>
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/pcac2908634-cac-iphone-13-pro-mlve3aa-a-256gb-graphite-apple-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="CAC IPHONE 13 PRO MLVE3AA/A 256GB GRAPHITE APPLE+ECOUTEURS FIL LIGHTNING EARPODS MMTN2ZM/A APPLE" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/2/9/2908634-2832636.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15409,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/pcac2908634-cac-iphone-13-pro-mlve3aa-a-256gb-graphite-apple-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        ECOUTEURS LIGHTNING EA...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15409" data-product-id="15409" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -2%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          16 169
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          15 790
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/pcac2908634-cac-iphone-13-pro-mlve3aa-a-256gb-graphite-apple-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15409,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15409","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_1" title="Indisponible">
        Indisponible
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <div class="remise-cac">
   <h3 class="title-cac-product">
    Bon de remise de
    <span>
     379
     <span class="currency">
      DH
     </span>
    </span>
   </h3>
  </div>
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/pcac2908610-cac-iphone-13-mlqc3aa-a-512gb-midnight-apple-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="CAC IPHONE 13 MLQC3AA/A 512GB MIDNIGHT APPLE+ECOUTEURS FIL LIGHTNING EARPODS MMTN2ZM/A APPLE" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/2/9/2908610-2832636.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15408,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/pcac2908610-cac-iphone-13-mlqc3aa-a-512gb-midnight-apple-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        ECOUTEURS LIGHTNING EA...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15408" data-product-id="15408" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -2%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          15 869
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          15 490
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/pcac2908610-cac-iphone-13-mlqc3aa-a-512gb-midnight-apple-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15408,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15408","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_1" title="Indisponible">
        Indisponible
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <div class="remise-cac">
   <h3 class="title-cac-product">
    Bon de remise de
    <span>
     379
     <span class="currency">
      DH
     </span>
    </span>
   </h3>
  </div>
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/pcac2908605-cac-iphone-13-mlq63aa-a-256gb-midnight-apple-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="CAC IPHONE 13 MLQ63AA/A 256GB MIDNIGHT APPLE+ECOUTEURS FIL LIGHTNING EARPODS MMTN2ZM/A APPLE" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/2/9/2908605-2832636.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15407,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/pcac2908605-cac-iphone-13-mlq63aa-a-256gb-midnight-apple-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        ECOUTEURS LIGHTNING EA...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15407" data-product-id="15407" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -2%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          13 169
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          12 790
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/pcac2908605-cac-iphone-13-mlq63aa-a-256gb-midnight-apple-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15407,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15407","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_1" title="Indisponible">
        Indisponible
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <div class="remise-cac">
   <h3 class="title-cac-product">
    Bon de remise de
    <span>
     379
     <span class="currency">
      DH
     </span>
    </span>
   </h3>
  </div>
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/pcac2908602-cac-iphone-13-mlph3aa-a-128gb-pink-appleapple-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="CAC IPHONE 13 MLPH3AA/A 128GB PINK APPLEAPPLE+ECOUTEURS FIL LIGHTNING EARPODS MMTN2ZM/A APPLE" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/2/9/2908602-2832636.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15406,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/pcac2908602-cac-iphone-13-mlph3aa-a-128gb-pink-appleapple-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        ECOUTEURS LIGHTNING EA...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15406" data-product-id="15406" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -3%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          11 628
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          11 249
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/pcac2908602-cac-iphone-13-mlph3aa-a-128gb-pink-appleapple-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15406,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15406","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_1" title="Indisponible">
        Indisponible
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <div class="remise-cac">
   <h3 class="title-cac-product">
    Bon de remise de
    <span>
     379
     <span class="currency">
      DH
     </span>
    </span>
   </h3>
  </div>
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/pcac2828074-cac-iphone-12-pro-max-128gb-pacific-blue-mgda3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="CAC IPHONE 12 PRO MAX 128GB PACIFIC BLUE  MGDA3AA/A+ECOUTEURS FIL LIGHTNING EARPODS MMTN2ZM/A APPLE" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/2/8/2828074-2832636.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15405,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/pcac2828074-cac-iphone-12-pro-max-128gb-pacific-blue-mgda3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        ECOUTEURS LIGHTNING EA...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15405" data-product-id="15405" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -2%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          15 978
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          15 599
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/pcac2828074-cac-iphone-12-pro-max-128gb-pacific-blue-mgda3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15405,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15405","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_1" title="Indisponible">
        Indisponible
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <div class="remise-cac">
   <h3 class="title-cac-product">
    Bon de remise de
    <span>
     379
     <span class="currency">
      DH
     </span>
    </span>
   </h3>
  </div>
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/pcac2828060-cac-iphone-12-pro-128gb-pacific-blue-mgmn3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="CAC IPHONE 12 PRO 128GB PACIFIC BLUE  MGMN3AA/A+ECOUTEURS FIL LIGHTNING EARPODS MMTN2ZM/A APPLE" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/2/8/2828060-2832636.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15402,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/pcac2828060-cac-iphone-12-pro-128gb-pacific-blue-mgmn3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        ECOUTEURS LIGHTNING EA...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15402" data-product-id="15402" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -2%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          13 378
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          12 999
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/pcac2828060-cac-iphone-12-pro-128gb-pacific-blue-mgmn3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15402,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15402","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_1" title="Indisponible">
        Indisponible
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <div class="remise-cac">
   <h3 class="title-cac-product">
    Bon de remise de
    <span>
     379
     <span class="currency">
      DH
     </span>
    </span>
   </h3>
  </div>
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/pcac2828059-cac-iphone-12-pro-128gb-graphite-mgmk3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="CAC IPHONE 12 PRO 128GB GRAPHITE  MGMK3AA/A+ECOUTEURS FIL LIGHTNING EARPODS MMTN2ZM/A APPLE" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/2/8/2828059-2832636.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15401,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/pcac2828059-cac-iphone-12-pro-128gb-graphite-mgmk3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        ECOUTEURS LIGHTNING EA...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15401" data-product-id="15401" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -2%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          14 678
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          14 299
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/pcac2828059-cac-iphone-12-pro-128gb-graphite-mgmk3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15401,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15401","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_1" title="Indisponible">
        Indisponible
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <div class="remise-cac">
   <h3 class="title-cac-product">
    Bon de remise de
    <span>
     379
     <span class="currency">
      DH
     </span>
    </span>
   </h3>
  </div>
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/pcac2828058-cac-iphone-12-pro-128gb-gold-mgmm3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="CAC IPHONE 12 PRO 128GB GOLD  MGMM3AA/A+ECOUTEURS FIL LIGHTNING EARPODS MMTN2ZM/A APPLE" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/2/8/2828058-2832636.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15400,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/pcac2828058-cac-iphone-12-pro-128gb-gold-mgmm3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        ECOUTEURS LIGHTNING EA...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15400" data-product-id="15400" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -2%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          13 378
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          12 999
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/pcac2828058-cac-iphone-12-pro-128gb-gold-mgmm3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15400,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15400","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_1" title="Indisponible">
        Indisponible
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <div class="remise-cac">
   <h3 class="title-cac-product">
    Bon de remise de
    <span>
     379
     <span class="currency">
      DH
     </span>
    </span>
   </h3>
  </div>
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/pcac2828039-cac-iphone-12-128gb-blue-mgje3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="CAC IPHONE 12 128GB BLUE  MGJE3AA/A+ECOUTEURS FIL LIGHTNING EARPODS MMTN2ZM/A APPLE" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/2/8/2828039-2832636.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15399,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/pcac2828039-cac-iphone-12-128gb-blue-mgje3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        ECOUTEURS LIGHTNING EA...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15399" data-product-id="15399" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -3%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          12 378
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          11 999
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/pcac2828039-cac-iphone-12-128gb-blue-mgje3aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15399,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15399","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_1" title="Indisponible">
        Indisponible
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p2827999-apple-iphone-11-128gb-black.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="APPLE IPHONE 11 128GB BLACK" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/i/p/iphone_11_black_2-up_vertical_us-en_screen_2.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":14398,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p2827999-apple-iphone-11-128gb-black.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        IPHONE 11 128GB BLACK
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-14398" data-product-id="14398" data-role="priceBox">
      <div class="special-price one_price">
       <span class="price-container price-final_price tax weee">
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          7 899
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </div>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p2827999-apple-iphone-11-128gb-black.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":14398,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"14398","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_1" title="Indisponible">
        Indisponible
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p2828039-apple-iphone-12-128go-bleu.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="APPLE IPHONE 12 128GO BLEU" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/i/p/iphone_12_blue_pure_front_iphone_12_blue_pure_back_2-up_screen__usen_3.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":14388,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p2828039-apple-iphone-12-128go-bleu.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        IPHONE 12 128GO BLEU
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-14388" data-product-id="14388" data-role="priceBox">
      <div class="special-price one_price">
       <span class="price-container price-final_price tax weee">
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          10 499
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </div>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p2828039-apple-iphone-12-128go-bleu.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":14388,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"14388","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_1" title="Indisponible">
        Indisponible
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p2828060-apple-iphone-12-pro-128-go-pacific-bleu.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="APPLE IPHONE 12 PRO 128 GO PACIFIC BLEU" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/i/p/iphone12pro_bleu_1.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":14331,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p2828060-apple-iphone-12-pro-128-go-pacific-bleu.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        IPHONE 12 PRO 128 GO P...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-14331" data-product-id="14331" data-role="priceBox">
      <div class="special-price one_price">
       <span class="price-container price-final_price tax weee">
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          12 999
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </div>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p2828060-apple-iphone-12-pro-128-go-pacific-bleu.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":14331,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"14331","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_1" title="Indisponible">
        Indisponible
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p2038164-remade-iphone-7-noir.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="REMADE IPHONE 7 32GO NOIR" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/2/0/2038164.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":10720,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p2038164-remade-iphone-7-noir.html">
       <span class="brand">
        REMADE
       </span>
       <span class="ref">
        IPHONE 7 32GO NOIR
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-10720" data-product-id="10720" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -10%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          3 890
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          3 500
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p2038164-remade-iphone-7-noir.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":10720,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"10720","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_1" title="Indisponible">
        Indisponible
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p1992375-remade-iphone-6-64go-gris.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="REMADE IPHONE 6 64GO GRIS" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/1/9/1992375.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":9047,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p1992375-remade-iphone-6-64go-gris.html">
       <span class="brand">
        REMADE
       </span>
       <span class="ref">
        IPHONE 6 64GO GRIS
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-9047" data-product-id="9047" data-role="priceBox">
      <div class="special-price one_price">
       <span class="price-container price-final_price tax weee">
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          2 590
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </div>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p1992375-remade-iphone-6-64go-gris.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":9047,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"9047","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_1" title="Indisponible">
        Indisponible
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p2009035-apple-iphone-6s-gold-64gb-remade.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="REMADE IPHONE 6S GOLD 64GB REMADE" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/2/0/2009035.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":8987,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p2009035-apple-iphone-6s-gold-64gb-remade.html">
       <span class="brand">
        REMADE
       </span>
       <span class="ref">
        IPHONE 6S GOLD 64GB REMADE
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-8987" data-product-id="8987" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -67%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          3 090
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          1 000
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p2009035-apple-iphone-6s-gold-64gb-remade.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":8987,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"8987","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_1" title="Indisponible">
        Indisponible
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <div class="remise-cac">
   <h3 class="title-cac-product">
    Bon de remise de
    <span>
     379
     <span class="currency">
      DH
     </span>
    </span>
   </h3>
  </div>
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/pcac2828035-cac-iphone-12-64gb-green-mgj93aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="CAC IPHONE 12 64GB GREEN  MGJ93AA/A+ECOUTEURS FIL LIGHTNING EARPODS MMTN2ZM/A APPLE" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/2/8/2828035-2832636.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15416,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/pcac2828035-cac-iphone-12-64gb-green-mgj93aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        ECOUTEURS LIGHTNING EA...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
       <span class="flag label-product promo">
        Promo
       </span>
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15416" data-product-id="15416" data-role="priceBox">
      <!-- start discount percent -->
      <span class="ep_discount_percent">
       -3%
      </span>
      <!-- end discount percent -->
      <span class="old-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix normal
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          10 069
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
      <span class="special-price">
       <span class="price-container price-final_price tax weee">
        <span class="price-label">
         Prix Spécial
        </span>
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          9 690
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </span>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/pcac2828035-cac-iphone-12-64gb-green-mgj93aa-a-ecouteurs-fil-lightning-earpods-mmtn2zm-a-apple.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15416,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15416","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_0" title="Epuisé">
        Epuisé
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p2908631-apple-iphone13-pro-128g-silver.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="APPLE IPHONE13 PRO 128G SILVER" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/i/p/iphone_13_pro_silver_pure_back_iphone_13_pro_silver_pure_front_2-up_screen__usen.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15118,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p2908631-apple-iphone13-pro-128g-silver.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        IPHONE13 PRO 128G SILVER
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15118" data-product-id="15118" data-role="priceBox">
      <div class="special-price one_price">
       <span class="price-container price-final_price tax weee">
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          14 290
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </div>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p2908631-apple-iphone13-pro-128g-silver.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15118,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15118","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_0" title="Epuisé">
        Epuisé
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p2908630-apple-iphone-13-pro-128g-graphite.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="APPLE IPHONE 13 PRO 128G GRAPHITE" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/i/p/iphone_13_pro_graphite_pure_back_iphone_13_pro_graphite_pure_front_2-up_screen__usen.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15117,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p2908630-apple-iphone-13-pro-128g-graphite.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        IPHONE 13 PRO 128G GRAPHITE
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15117" data-product-id="15117" data-role="priceBox">
      <div class="special-price one_price">
       <span class="price-container price-final_price tax weee">
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          14 290
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </div>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p2908630-apple-iphone-13-pro-128g-graphite.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15117,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15117","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_0" title="Epuisé">
        Epuisé
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p2908633-apple-iphone-13-pro-128g-sierra-bleu.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="APPLE IPHONE 13 PRO 128G SIERRA BLEU" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/s/i/sierra_bleu.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15116,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p2908633-apple-iphone-13-pro-128g-sierra-bleu.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        IPHONE 13 PRO 128G SIE...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15116" data-product-id="15116" data-role="priceBox">
      <div class="special-price one_price">
       <span class="price-container price-final_price tax weee">
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          14 290
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </div>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p2908633-apple-iphone-13-pro-128g-sierra-bleu.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15116,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15116","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_0" title="Epuisé">
        Epuisé
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p2908632-apple-iphone-13-pro-128g-gold.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="APPLE IPHONE 13 PRO 128G GOLD" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/i/p/iphone_13_pro_gold_pure_back_iphone_13_pro_gold_pure_front_2-up_screen__usen.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15115,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p2908632-apple-iphone-13-pro-128g-gold.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        IPHONE 13 PRO 128G GOLD
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15115" data-product-id="15115" data-role="priceBox">
      <div class="special-price one_price">
       <span class="price-container price-final_price tax weee">
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          14 290
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </div>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p2908632-apple-iphone-13-pro-128g-gold.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15115,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15115","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_0" title="Epuisé">
        Epuisé
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p2908635-apple-iphone-13-pro-256g-silver.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="APPLE IPHONE 13 PRO 256G SILVER" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/i/p/iphone_13_pro_silver_pure_back_iphone_13_pro_silver_pure_front_2-up_screen__usen_1.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15112,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p2908635-apple-iphone-13-pro-256g-silver.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        IPHONE 13 PRO 256G SILVER
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15112" data-product-id="15112" data-role="priceBox">
      <div class="special-price one_price">
       <span class="price-container price-final_price tax weee">
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          15 790
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </div>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p2908635-apple-iphone-13-pro-256g-silver.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15112,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15112","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_0" title="Epuisé">
        Epuisé
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p2908634-apple-iphone-13-pro-256g-graphite.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="APPLE IPHONE 13 PRO 256G GRAPHITE" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/i/p/iphone_13_pro_graphite_pure_back_iphone_13_pro_graphite_pure_front_2-up_screen__usen_1.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15111,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p2908634-apple-iphone-13-pro-256g-graphite.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        IPHONE 13 PRO 256G GRAPHITE
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15111" data-product-id="15111" data-role="priceBox">
      <div class="special-price one_price">
       <span class="price-container price-final_price tax weee">
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          15 790
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </div>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p2908634-apple-iphone-13-pro-256g-graphite.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15111,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15111","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_0" title="Epuisé">
        Epuisé
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p2908637-apple-iphone-13-pro-256g-sierra-bleu.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="APPLE IPHONE 13 PRO 256G SIERRA BLEU" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/s/i/sierra_bleu_1.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15110,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p2908637-apple-iphone-13-pro-256g-sierra-bleu.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        IPHONE 13 PRO 256G SIE...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15110" data-product-id="15110" data-role="priceBox">
      <div class="special-price one_price">
       <span class="price-container price-final_price tax weee">
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          15 790
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </div>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p2908637-apple-iphone-13-pro-256g-sierra-bleu.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15110,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15110","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_0" title="Epuisé">
        Epuisé
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p2908636-apple-iphone-13-pro-256go-gold.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="APPLE IPHONE 13 PRO 256GO GOLD" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/i/p/iphone_13_pro_gold_pure_back_iphone_13_pro_gold_pure_front_2-up_screen__usen_1.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15109,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p2908636-apple-iphone-13-pro-256go-gold.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        IPHONE 13 PRO 256GO GOLD
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15109" data-product-id="15109" data-role="priceBox">
      <div class="special-price one_price">
       <span class="price-container price-final_price tax weee">
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          15 790
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </div>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p2908636-apple-iphone-13-pro-256go-gold.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15109,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15109","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_0" title="Epuisé">
        Epuisé
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
 <li class="item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12">
  <!-- start cac discount -->
  <!-- end cac discount -->
  <div class="product-item-info" data-container="product-grid">
   <div class="item-inner">
    <div class="box-image">
     <a class="product photo product-item-photo" href="https://www.electroplanet.ma/p2908649-apple-iphone-13-pro-max-128g-sierra-bleu.html" tabindex="-1">
      <span class="product-image-container">
       <span class="product-image-wrapper">
        <img alt="APPLE IPHONE 13 PRO MAX 128G SIERRA BLEU" class="product-image-photo" data-lazy="https://media.electroplanet.ma/pub/media/catalog/product/cache/14e469c4a70431355c88f88fd8855f6e/s/i/sierra_bleu_4.jpg" height="" width=""/>
       </span>
      </span>
     </a>
     <div class="bottom-action">
      <!-- <a href="#" class="action towishlist btn-action link-wishlist" data-toggle="tooltip" data-placement="left" title="Ajouter à ma liste d’envie"  aria-label="Ajouter à ma liste d’envie" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15103,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-action="add-to-wishlist"  role="button">
												<span>Ajouter à ma liste d’envie</span>
											</a> -->
     </div>
    </div>
    <div class="product details product-item-details box-info">
     <strong class="product-item-sub-category ref">
      iPhone
     </strong>
     <div class="product name product-item-name product-name">
      <a class="product-item-link" href="https://www.electroplanet.ma/p2908649-apple-iphone-13-pro-max-128g-sierra-bleu.html">
       <span class="brand">
        APPLE
       </span>
       <span class="ref">
        IPHONE 13 PRO MAX 128G...
       </span>
      </a>
      <!-- start stickers -->
      <!-- start stickers -->
      <div class="flag_list">
      </div>
      <!-- end stickers -->
      <!-- end stickers -->
     </div>
     <div class="price-box price-final_price" data-price-box="product-id-15103" data-product-id="15103" data-role="priceBox">
      <div class="special-price one_price">
       <span class="price-container price-final_price tax weee">
        <!-- override existing class to show all time TTC symbol-->
        <span class="price-wrapper">
         <span class="price">
          15 490
         </span>
         <span class="currency">
          DH
         </span>
        </span>
       </span>
      </div>
     </div>
     <div class="product-item-inner">
     </div>
     <!-- Bottom Action -->
     <div class="bottom_action">
      <!-- Product Link -->
      <a class="product-link" href="https://www.electroplanet.ma/p2908649-apple-iphone-13-pro-max-128g-sierra-bleu.html">
       VOIR LE PRODUIT
      </a>
      <!-- End: Product Link -->
      <!-- Link Wishlist -->
      <a class="add-to-wishlist action tocompare btn-action link-wishlist" data-action="add-to-wishlistoo" data-post='{"action":"https:\/\/www.electroplanet.ma\/wishlist\/index\/add\/","data":{"product":15103,"uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' href="javascript:void(0)" title="Ajouter à ma liste">
       <span>
        AJOUTER A MA LISTE
       </span>
      </a>
      <!-- End: Link Wishlist -->
      <!-- Link Compare -->
      <a class="comparer-product action tocompare btn-action link-compare" data-placement="top" data-post='{"action":"https:\/\/www.electroplanet.ma\/catalog\/product_compare\/add\/","data":{"product":"15103","uenc":"aHR0cHM6Ly93d3cuZWxlY3Ryb3BsYW5ldC5tYS9zbWFydHBob25lLXRhYmxldHRlLWdwcy9zbWFydHBob25lL2lwaG9uZT9wcm9kdWN0X2xpc3RfbGltaXQ9NjA,"}}' data-toggle="tooltip" href="javascript:void(0)" role="button" title="Ajouter au comparateur">
       <span>
        Ajouter au comparateur
       </span>
      </a>
      <!-- End: Link compare -->
      <div class="stock-status-wrapper">
       <span class="stock-status stock_status_0" title="Epuisé">
        Epuisé
       </span>
      </div>
     </div>
     <!-- End: Bottom Action -->
    </div>
   </div>
  </div>
 </li>
</ol>
"""

list_items = BS(
    list_items ,
    features="html.parser"
)

stockage_list = ['32 Go','32G', '32 Gb','128 Gb','128G','256 Gb','512 Gb','512G','1 Tb','1T' ,'128 Go','256 Go','256G','512 Go','512G', '1 To' , '64 Go' ,'64G', '64 Gb' ]
iphones = ['iPhone 13 Pro Max','iPhone 13 Pro','iPhone 12 Mini','iPhone 11 PRO MAX','iPhone 11 PRO','iPhone 11','iPhone 8 Plus','iPhone 7','iPhone se','iPhone Xr' , 'IPHONE 12 PRO MAX']
colors = ['Bleu Alpin' , 'Graphite', 'Or' , 'Argent', 'Argent', 'Rose', 'Bleu' , 'Minuit' , 'Noir' , 'Blanc' , 'Rouge', 'Vert Nuit','Vert', 'Jaune', 'GOLD' , 'SILVER', 'BLACK', 'MIDNIGHT','PACIFIC BLU' , 'GREEN' , 'PINK' , 'GRIS'  ]
now = datetime.datetime.now()
scraped_at = "{}-{}-{} {}:{}:{}".format(now.year, now.month, now.day, now.hour, now.minute, now.second)

def get_device_name(fullDeveiceName):
    for iphone in iphones:
        if iphone.upper() in fullDeveiceName:
            return iphone
    return  fullDeveiceName

def format_price(price):
    tmp = price.split()
    floatprice = "".join(tmp)
    return float(floatprice)

def find_device_stockage(title):
    for st in stockage_list:
        if st.upper() in title:
            return st

    return "UNKNOWN"

def find_device_color(title):
    for c in colors:
        if c.upper() in title:
            return c

    return "UNKNOWN"




list_items = list_items.findAll('li' , {'class' , 'item product product-item col-lg-3 col-md-3 col-sm-4 col-xs-12'})
# print(list_items)
for num, it in enumerate(list_items):
    item_title =  it.find('img' , {'class' , 'product-image-photo'}).get('alt')
    item_image = it.find('img', {'class' , 'product-image-photo'}).get('src')
    item_slug = get_device_name(item_title)
    try:
        tmp = it.findAll('span', {'class', 'price'})[1]
    except:
        tmp = it.findAll('span', {'class', 'price'})[0]

    item_link = it.find('a' , {'class' , 'product photo product-item-photo'}).get('href')
    item_stockage = find_device_stockage(item_title)
    item_color = find_device_color(item_title)
    print("==================={}=====================".format(num+1))
    print("item_link = {}".format(item_link))
    print("item_title = {}".format(item_title) )
    print("item_image = {}".format(item_image))
    print("item_slug = {}".format(item_slug))
    print("item_price = {}".format(
        format_price(
            (tmp.get_text()).strip()
        )
    ))
    print("item_stockage={}".format(item_stockage))
    print("iteam_color={}".format(item_color))
    print("scrapped_at = {}".format(scraped_at))

    print("\n")
    try:
        shoudl_I_insert_to_db = True
        myjson = dict()
        myjson["stockage"] = item_stockage
        myjson["color"] = item_color
        jsonStringify = json.dumps(myjson, indent=4, sort_keys=True, default=str)

        sql = "select current_price from items where slug = %s"
        val = (item_title)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        if(len(myresult) == 0):
            sql = "INSERT INTO items (name ,slug,link, id_store ,id_category ,specification ,details ,image_url,current_price,last_updated_at) VALUES (%s, %s, %s, %s, %s ,%s ,%s,%s ,%s, %s)"
            val = ("iPhone 7",item_title, item_link, 1, 1, jsonStringify, "", image_item, item_price,scraped_at)
            mycursor.execute(sql, val)
            print("id = {}".format(
                mycursor.lastrowid
            ))
            sql = "INSERT INTO prices (id_item ,price,created_at) VALUES (%s, %s, %s)"
            val = (mycursor.lastrowid, item_price, scraped_at)
            mycursor.execute(sql, val)
            print("\n")
            mydb.commit()
        else:
            if(myresult[0][0] != item_price ):
                sql = "update items set current_price = %s , last_updated_at = %s where slug = %s"
                val = (item_price , scraped_at , item_title)
                mycursor.execute(sql, val)
                sql = "select id from items where slug = %s"
                val = (item_title,)
                myresult = mycursor.fetchall()
                sql = "insert into prices (id_item ,price,created_at) VALUES (%s, %s, %s)"
                val = (myresult[0][0], item_price, scraped_at)
                mydb.commit()
            else:
                print("PRICES ARE STILL THE SAME")
                print(" -> {} == {}".format(myresult[0][0] , item_price))

    except Exception as e:
        print(e)
        print("Database conn error !")


    mydb.close()


