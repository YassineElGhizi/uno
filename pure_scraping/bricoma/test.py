import json

import requests

import json
import pymysql
import requests
from bs4 import BeautifulSoup as BS
from time import sleep
import datetime
import random



html ="""
<!DOCTYPE html>
<html dir="ltr" lang="fr-MA">
 <head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1" name="viewport"/>
  <meta content="ie=edge" http-equiv="X-UA-Compatible"/>
  <meta content="index, follow" name="robots"/>
  <meta content="Meubles" name="description"/>
  <meta content="Meubles" name="keywords"/>
  <meta content="Meubles" property="og:title"/>
  <meta content="product.group" property="og:type"/>
  <meta content="https://www.ikea.com/ma/fr/cat/meubles-fu001/" property="og:url"/>
  <meta content="IKEA" property="og:site_name"/>
  <meta content="Meubles" property="og:description"/>
  <meta content="https://shop.static.ingka.ikea.com/category-images/Category_armchairs-and-chaise-longues.jpg" property="og:image"/>
  <title>
   Meubles - IKEA
  </title>
  <link href="https://www.ikea.com/ma/fr/cat/meubles-fu001/" rel="canonical"/>
  <link as="script" href="https://www.ikea.com/ma/fr/product-lists/plp-main-716.js" rel="preload"/>
  <link href="https://www.ikea.com/ma/fr/product-lists/plp-main-716.css" rel="stylesheet"/>
  <link href="/ma/fr/stylesheets/vendors.f3da27d99d540eacd13e.css" rel="stylesheet"/>
  <link href="/ma/fr/stylesheets/main.39214ff393a5f066b515.css" rel="stylesheet"/>
  <link href="https://www.ikea.com/ma/fr/products/stylesheets/price-package-styles.b6db989bce7060d77263.css" rel="stylesheet"/>
  <!-- 2022-02-15T07:25:32.128Z, Navigera 2a15d589 -->
  <link data-opti-default="true" data-opti-edge="false" data-opti-web="true" href="https://www.ikea.com/ma/fr/header-footer/styles/main.68c17abda7601a643045.css" id="nav-styles" rel="stylesheet"/>
  <link as="font" crossorigin="" href="https://www.ikea.com/global/assets/fonts/woff2/noto-ikea-400.latin.16880ce8.woff2" rel="preload" type="font/woff2"/>
  <link as="font" crossorigin="" href="https://www.ikea.com/global/assets/fonts/woff2/noto-ikea-700.latin.5d09a799.woff2" rel="preload" type="font/woff2"/>
  <link href="https://www.ikea.com/global/assets/fonts/fr/fonts.6cf91fe6.css" rel="stylesheet"/>
  <!-- Search Box Styles: 2022-02-11 7:54:07 CET refs/tags/v8.200.0-3d21032ab0cf4bf06e56d7f2934eb683a2957c59 -->
  <link href="https://www.ikea.com/ma/fr/search/box-legacy.a1aa2c5b.css" rel="stylesheet"/>
  <link href="https://www.ikea.com/ma/fr/search/box.a1aa2c5b.css" rel="stylesheet"/>
  <!-- /Search Box Styles -->
  <!-- RecommendationsStyle: version: 6b92168, site-folder: ma/fr -->
  <link href="https://www.ikea.com/ma/fr/recommendations/panels/rec.5c136546.css" rel="stylesheet"/>
  <!-- /RecommendationsStyle -->
  <!-- gitVersion: 20220214052700, siteFolder: ma/fr -->
  <link href="https://www.ikea.com/ma/fr/insp-feed/content-gallery-app/feed.b7bf7399.css" rel="stylesheet"/>
  <script async="" src="https://www.ikea.com/resources/d8b81cb1eca30f9e47bbd5dca6ad17184ef84d02a8c7a" type="text/javascript">
  </script>
  <script async="" src="https://www.ikea.com/ext/optimizelyjs/s/morocco_web.js">
  </script>
  <link href="https://www.ikea.com/ma/fr/static/favicon.838d8a3778e4d716eb72.ico" rel="shortcut icon"/>
  <meta content="max-image-preview:large" name="robots"/>
  <!-- empty -->
  <script data-type="utag-data">
   var utag_data = {"site_platform":"m2","visit_country":"ma","visit_language":"fr","page_type":"product listing","site_section":"product listing>fu001","page_name":"no_page_name","page_category_level":"top_category"}
  </script>
  <noscript>
   <style>
    .js-product-list { display: none }
   </style>
  </noscript>
 </head>
 <body class="product-listing-page" data-is-range-page="true">
  <!-- 2022-02-15T07:25:32.136Z, Navigera 2a15d589 -->
  <a class="hnf-skip-to-content hnf-link" href="#hnf-content">
   Aller au contenu principal
  </a>
  <div class="hnf-messages">
   <div class="hnf-message" id="value-proposition-message">
   </div>
   <div class="hnf-message" id="shoppable-app-message">
   </div>
  </div>
  <div class="hnf-header-hamburger hnf-page-container">
   <div class="hnf-page-container__inner">
    <div class="hnf-page-container__aside">
     <button aria-label="Menu" class="hnf-btn hnf-btn--small hnf-btn--icon-tertiary" title="Menu" type="button">
      <span class="hnf-btn__inner">
       <svg class="svg-icon hnf-svg-icon" fill="none" focusable="false" height="24" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
        <path clip-rule="evenodd" d="M20 8H4V6h16v2zm0 5H4v-2h16v2zm0 5H4v-2h16v2z" fill-rule="evenodd">
        </path>
       </svg>
      </span>
     </button>
    </div>
   </div>
  </div>
  <header class="hnf-header hnf-header--store hnf-header--2nd-line">
   <div class="hnf-page-container">
    <div class="hnf-page-container__inner">
     <div class="hnf-header__container hnf-page-container__main">
      <div class="hnf-header__logo">
       <a class="hnf-link" data-tracking-label="ikea-logo" href="https://www.ikea.com/ma/fr/">
        <img alt="IKEA" src="https://www.ikea.com/ma/fr/static/ikea-logo.f7d9229f806b59ec64cb.svg" title="IKEA"/>
        <span class="hnf-header__sr-only">
         IKEA
        </span>
       </a>
      </div>
      <div class="hnf-header__search">
       <div data-baseurl="https://www.ikea.com" data-css-scope="search-box" data-locale="fr-MA" data-namespace="search-box" data-version="refs/tags/v8.200.0-3d21032ab0cf4bf06e56d7f2934eb683a2957c59">
        <div class="notranslate">
         <form action="https://www.ikea.com/ma/fr/search/" class="search-box" role="search">
          <div class="search-wrapper">
           <div class="search-field">
            <svg aria-hidden="true" class="svg-icon search-field__search-icon search-field__search-icon--show" height="24" width="24">
             <path clip-rule="evenodd" d="M13.98 15.395a6.294 6.294 0 111.414-1.414l4.602 4.601-1.414 1.414-4.602-4.601zm.607-5.101a4.294 4.294 0 11-8.587 0 4.294 4.294 0 018.587 0z" fill="#111" fill-rule="evenodd">
             </path>
            </svg>
            <span class="search-box__button-wrapper-close-icon">
            </span>
            <input aria-label="Trouver des articles, des nouveautés ou des idées inspirantes" aria-placeholder="Rechercher par produits, inspiration ou nouveautés" autocapitalize="off" autocomplete="off" autocorrect="off" class="search-field__input" maxlength="150" name="q" placeholder="Que cherchez-vous?" type="search"/>
            <span class="search-box__button-wrapper">
            </span>
           </div>
          </div>
         </form>
        </div>
       </div>
      </div>
      <ul class="hnf-header__icons" data-shopping-links="">
       <li class="hnf-header__search-btn">
        <button aria-expanded="false" aria-label="Rechercher" class="hnf-btn hnf-btn--small hnf-btn--icon-tertiary" title="Rechercher" type="button">
         <span class="hnf-btn__inner">
          <svg class="svg-icon hnf-svg-icon" fill="none" focusable="false" height="24" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
           <path clip-rule="evenodd" d="M13.9804 15.3946c-1.0361.7502-2.3099 1.1925-3.6869 1.1925C6.8177 16.5871 4 13.7694 4 10.2935 4 6.8177 6.8177 4 10.2935 4c3.4759 0 6.2936 2.8177 6.2936 6.2935 0 1.377-.4423 2.6508-1.1925 3.6869l4.6016 4.6016-1.4142 1.4142-4.6016-4.6016zm.6067-5.1011c0 2.3713-1.9223 4.2936-4.2936 4.2936C7.9223 14.5871 6 12.6648 6 10.2935 6 7.9223 7.9223 6 10.2935 6c2.3713 0 4.2936 1.9223 4.2936 4.2935z" fill-rule="evenodd">
           </path>
          </svg>
         </span>
        </button>
       </li>
       <li class="hnf-location__container" data-hide-hours="false" data-hours-default="Voir les heures d'ouverture" data-hours-open-today="Ouvert aujourd’hui {{from - to}}" data-hours-open-tomorrow="Ouvert demain {{from - to}}" data-hours-open-until="Ouvert jusqu'à {{closing time}}" data-ip-lookup="false" data-preselected-store="269" data-save-loc="false" data-see-hours-and-more="See hours and more" data-select-store="Choisir un magasin" id="hnf-header-storepicker">
        <button class="hnf-location__store hnf-btn">
         <svg class="svg-icon hnf-svg-icon" fill="none" focusable="false" height="24" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
          <path clip-rule="evenodd" d="M22 20V4H2v16h20zM20 6H4v12h3v-8h10v8h3V6zm-9 6H9v6h2v-6zm2 6h2v-6h-2v6z" fill-rule="evenodd">
          </path>
         </svg>
         <div class="hnf-location__textwrapper">
          <small>
           See hours and more
          </small>
          <strong>
           Choisir un magasin
          </strong>
         </div>
        </button>
       </li>
       <li class="hnf-header__profile-link">
        <a aria-label="Mon profil" class="hnf-btn hnf-btn--small hnf-btn--icon-tertiary" data-profile-link="" data-tracking-label="profile" href="https://secure.ikea.com/webapp/wcs/stores/servlet/LogonForm?storeId=55&amp;langId=-81" rel="nofollow" title="Mon profil">
         <span class="hnf-btn__inner">
          <svg class="svg-icon hnf-svg-icon hnf-btn__icon hnf-person__icon" fill="none" focusable="false" height="24" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
           <path clip-rule="evenodd" d="M10.6724 6.4678c.2734-.2812.6804-.4707 1.3493-.4707.3971 0 .705.0838.9529.2225.241.1348.4379.3311.5934.6193l.0033.006c.1394.2541.237.6185.237 1.1403 0 .7856-.2046 1.2451-.4796 1.5278l-.0048.005c-.2759.2876-.679.4764-1.334.4764-.3857 0-.6962-.082-.956-.2241-.2388-.1344-.4342-.3293-.5888-.6147-.1454-.275-.2419-.652-.2419-1.1704 0-.7902.2035-1.2442.4692-1.5174zm1.3493-2.4717c-1.0834 0-2.054.3262-2.7838 1.0766-.7376.7583-1.0358 1.781-1.0358 2.9125 0 .7656.1431 1.483.4773 2.112l.0031.0058c.3249.602.785 1.084 1.3777 1.4154l.0062.0035c.5874.323 1.2368.4736 1.9235.4736 1.0818 0 2.0484-.3333 2.7755-1.0896.7406-.7627 1.044-1.786 1.044-2.9207 0-.7629-.1421-1.4784-.482-2.0996-.3247-.6006-.7844-1.0815-1.376-1.4125-.5858-.3276-1.2388-.477-1.9297-.477zM6.4691 16.8582c.2983-.5803.7228-1.0273 1.29-1.3572.5582-.3191 1.2834-.5049 2.2209-.5049h4.04c.9375 0 1.6626.1858 2.2209.5049.5672.3299.9917.7769 1.29 1.3572.3031.5896.4691 1.2936.4691 2.1379v1h2v-1c0-1.1122-.2205-2.1384-.6904-3.0523a5.3218 5.3218 0 0 0-2.0722-2.1769c-.9279-.5315-2.0157-.7708-3.2174-.7708H9.98c-1.1145 0-2.2483.212-3.2225.7737-.8982.5215-1.5928 1.2515-2.0671 2.174C4.2205 16.8577 4 17.8839 4 18.9961v1h2v-1c0-.8443.166-1.5483.4691-2.1379z" fill-rule="evenodd">
           </path>
          </svg>
          <svg class="svg-icon hnf-svg-icon hnf-btn__icon hnf-person-active__icon hnf-person-active__icon--hidden" fill="none" focusable="false" height="24" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
           <path d="M21 17.5c0 1.3807-1.1193 2.5-2.5 2.5S16 18.8807 16 17.5s1.1193-2.5 2.5-2.5 2.5 1.1193 2.5 2.5z" fill="#0058A3">
           </path>
           <path clip-rule="evenodd" d="M9.2379 5.0727c.7298-.7504 1.7004-1.0766 2.7838-1.0766.6909 0 1.3439.1494 1.9297.477.5916.331 1.0513.8119 1.376 1.4125.3399.6212.482 1.3367.482 2.0996 0 1.1348-.3034 2.158-1.044 2.9207-.7271.7563-1.6937 1.0896-2.7755 1.0896-.6867 0-1.3361-.1506-1.9235-.4736l-.0062-.0035c-.5927-.3314-1.0528-.8134-1.3777-1.4154l-.0031-.0058c-.3342-.629-.4772-1.3464-.4772-2.112 0-1.1315.2981-2.1542 1.0357-2.9125zm2.7838.9245c-.6689 0-1.0759.1894-1.3493.4706-.2657.2732-.4692.7272-.4692 1.5174 0 .5185.0965.8953.2419 1.1704.1546.2854.35.4803.5888.6147.2598.1421.5703.2241.956.2241.655 0 1.0581-.1888 1.334-.4764l.0048-.005c.275-.2827.4796-.7422.4796-1.5278 0-.5218-.0976-.8862-.237-1.1404l-.0033-.0059c-.1555-.2882-.3524-.4845-.5934-.6193-.2479-.1387-.5558-.2224-.9529-.2224z" fill-rule="evenodd">
           </path>
           <path d="M7.759 15.501c-.5671.3299-.9916.7769-1.2899 1.3572C6.166 17.4478 6 18.1518 6 18.9961v1H4v-1c0-1.1122.2205-2.1384.6904-3.0523.4743-.9225 1.1689-1.6525 2.0671-2.174.9742-.5617 2.108-.7737 3.2225-.7737h4.04c.82 0 1.587.1114 2.2863.3511l-1.6773 1.6773a6.2932 6.2932 0 0 0-.609-.0284H9.98c-.9375 0-1.6627.1858-2.221.5049z">
           </path>
          </svg>
          <span class="hnf-btn__label">
           Mon profil
          </span>
         </span>
        </a>
       </li>
       <li class="hnf-header__shopping-list-link" data-shoppinglist-icon="favorite">
        <a aria-label="Favoris" class="hnf-btn hnf-btn--small hnf-btn--icon-tertiary" data-tracking-label="shopping-list" href="https://order.ikea.com/ma/fr/checkout/shoppinglist/" rel="nofollow" title="Favoris">
         <span class="hnf-btn__inner">
          <svg class="svg-icon hnf-svg-icon hnf-btn__icon" fill="none" focusable="false" height="24" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
           <path clip-rule="evenodd" d="M12.336 5.52055C14.2336 3.62376 17.3096 3.62401 19.2069 5.52129C20.2067 6.52115 20.6796 7.85005 20.6259 9.15761C20.6151 12.2138 18.4184 14.8654 16.4892 16.6366C15.4926 17.5517 14.5004 18.2923 13.7593 18.8036C13.3879 19.0598 13.0771 19.2601 12.8574 19.3973C12.7475 19.466 12.6601 19.519 12.5992 19.5555C12.5687 19.5737 12.5448 19.5879 12.5279 19.5978L12.5079 19.6094L12.502 19.6129L12.5001 19.614C12.5001 19.614 12.4989 19.6147 11.9999 18.748C11.501 19.6147 11.5005 19.6144 11.5005 19.6144L11.4979 19.6129L11.4919 19.6094L11.472 19.5978C11.4551 19.5879 11.4312 19.5737 11.4007 19.5555C11.3397 19.519 11.2524 19.466 11.1425 19.3973C10.9227 19.2601 10.612 19.0598 10.2405 18.8036C9.49947 18.2923 8.50726 17.5517 7.51063 16.6366C5.58146 14.8654 3.38477 12.2139 3.37399 9.15765C3.32024 7.85008 3.79314 6.52117 4.79301 5.52129C6.69054 3.62376 9.76704 3.62376 11.6646 5.52129L11.9993 5.856L12.3353 5.52129L12.336 5.52055ZM11.9999 18.748L11.5005 19.6144L11.9999 19.9019L12.4989 19.6147L11.9999 18.748ZM11.9999 17.573C12.1727 17.462 12.384 17.3226 12.6236 17.1573C13.3125 16.6821 14.2267 15.9988 15.1366 15.1634C17.0157 13.4381 18.6259 11.2919 18.6259 9.13506V9.11213L18.627 9.08922C18.6626 8.31221 18.3844 7.52727 17.7926 6.9355C16.6762 5.81903 14.866 5.81902 13.7495 6.9355L13.7481 6.93689L11.9965 8.68166L10.2504 6.9355C9.13387 5.81903 7.3237 5.81903 6.20722 6.9355C5.61546 7.52727 5.33724 8.31221 5.3729 9.08922L5.37395 9.11213V9.13507C5.37395 11.2919 6.98418 13.4381 8.86325 15.1634C9.77312 15.9988 10.6874 16.6821 11.3762 17.1573C11.6159 17.3226 11.8271 17.462 11.9999 17.573Z" fill-rule="evenodd">
           </path>
          </svg>
          <span class="hnf-btn__label">
           Favoris
          </span>
         </span>
        </a>
       </li>
       <li class="hnf-header__shopping-cart-link">
        <a aria-label="Panier" class="hnf-btn hnf-btn--small hnf-btn--icon-tertiary" data-tracking-label="shopping-bag" href="https://secure.ikea.com/ma/fr/mcommerce/shoppingcart" rel="nofollow" title="Panier">
         <span class="hnf-btn__inner js-shopping-cart-icon" data-market-code="fr-MA">
          <span class="hnf-header__cart-counter" style="display:none">
          </span>
          <svg class="svg-icon hnf-svg-icon hnf-svg-bag-default hnf-btn__icon" fill="none" focusable="false" height="24" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
           <path clip-rule="evenodd" d="M10.9994 4h-.5621l-.2922.4802-3.357 5.517h-5.069l.3107 1.2425 1.6212 6.4851c.334 1.3355 1.5339 2.2724 2.9105 2.2724h10.8769c1.3766 0 2.5765-.9369 2.9104-2.2724l1.6213-6.4851.3106-1.2425h-5.0695l-3.3574-5.517L13.5618 4h-2.5624zm3.8707 5.9972L12.4376 6h-.8761L9.1292 9.9972h5.7409zm-9.2787 7.2425-1.3106-5.2425h15.4384l-1.3106 5.2425a1 1 0 0 1-.9701.7575H6.5615a1 1 0 0 1-.97-.7575z" fill-rule="evenodd">
           </path>
          </svg>
          <span class="hnf-btn__label">
           Panier
          </span>
         </span>
        </a>
       </li>
       <li class="hnf-header__hamburger">
        <button aria-expanded="false" aria-label="Menu" class="hnf-btn hnf-btn--small hnf-btn--icon-tertiary" title="Menu" type="button">
         <span class="hnf-btn__inner">
          <svg class="svg-icon hnf-svg-icon hnf-btn__icon" fill="none" focusable="false" height="24" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
           <path clip-rule="evenodd" d="M20 8H4V6h16v2zm0 5H4v-2h16v2zm0 5H4v-2h16v2z" fill-rule="evenodd">
           </path>
          </svg>
         </span>
        </button>
       </li>
      </ul>
     </div>
    </div>
   </div>
  </header>
  <div id="hnf-header-filler">
  </div>
  <div class="hnf-page-container hnf-2nd-line">
   <div class="hnf-page-container__inner">
    <div class="hnf-header__container hnf-page-container__main">
     <nav class="hnf-header__nav">
      <ul class="hnf-header__nav__main" data-header-links="">
       <li>
        <a class="hnf-link" data-index="0" href="#">
         Des solutions abordables
        </a>
       </li>
       <li>
        <a class="hnf-link" data-index="1" data-products-link="" href="https://www.ikea.com/ma/fr/cat/products-products/">
         Produits
        </a>
       </li>
       <li>
        <a class="hnf-link" data-index="2" href="https://www.ikea.com/ma/fr/rooms/">
         Achetez par pièce
        </a>
       </li>
      </ul>
     </nav>
    </div>
   </div>
  </div>
  <div class="hnf-location hnf-storepicker">
   <div class="hnf-page-container">
    <div class="hnf-page-container__inner">
     <div class="hnf-location__container hnf-page-container__main">
      <button class="hnf-location__store hnf-btn">
       <svg class="svg-icon hnf-svg-icon" fill="none" focusable="false" height="24" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
        <path clip-rule="evenodd" d="M22 20V4H2v16h20zM20 6H4v12h3v-8h10v8h3V6zm-9 6H9v6h2v-6zm2 6h2v-6h-2v6z" fill-rule="evenodd">
        </path>
       </svg>
       <div class="hnf-location__textwrapper">
        <strong>
         Choisir un magasin
        </strong>
        <small>
         See hours and more
        </small>
       </div>
      </button>
     </div>
    </div>
   </div>
  </div>
  <aside aria-hidden="true" class="hnf-menu hnf-menu--default hnf-menu--hidden" data-title-more="Autres">
   <div class="hnf-menu__top">
    <div class="hnf-menu__close">
     <button aria-expanded="true" aria-label="Fermer menu" class="hnf-btn hnf-btn--small hnf-btn--icon-tertiary" id="hnf-menu-close-btn" title="Fermer menu" type="button">
      <span class="hnf-btn__inner">
       <svg class="svg-icon hnf-svg-icon" fill="none" focusable="false" height="24" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
        <path clip-rule="evenodd" d="m11.9997 13.4149 4.9498 4.9497 1.4142-1.4142-4.9498-4.9497 4.9498-4.9498-1.4142-1.4142-4.9498 4.9498L7.05 5.6367 5.6357 7.051l4.9498 4.9498-4.9497 4.9497L7.05 18.3646l4.9497-4.9497z" fill-rule="evenodd">
        </path>
       </svg>
      </span>
     </button>
    </div>
    <div class="hnf-menu__logo">
     <a class="hnf-link" data-tracking-label="ikea-logo" href="https://www.ikea.com/ma/fr/">
      <img alt="IKEA" src="https://www.ikea.com/ma/fr/static/ikea-logo.f7d9229f806b59ec64cb.svg" title="IKEA"/>
      <span class="hnf-menu__sr-only">
       IKEA
      </span>
     </a>
    </div>
    <div class="hnf-menu__search">
     <button aria-expanded="false" class="hnf-btn hnf-btn--small hnf-btn--icon-tertiary" id="hnf-menu-search-btn" title="Rechercher" type="button">
      <span class="hnf-btn__inner">
       <svg class="svg-icon hnf-svg-icon" fill="none" focusable="false" height="24" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
        <path clip-rule="evenodd" d="M13.9804 15.3946c-1.0361.7502-2.3099 1.1925-3.6869 1.1925C6.8177 16.5871 4 13.7694 4 10.2935 4 6.8177 6.8177 4 10.2935 4c3.4759 0 6.2936 2.8177 6.2936 6.2935 0 1.377-.4423 2.6508-1.1925 3.6869l4.6016 4.6016-1.4142 1.4142-4.6016-4.6016zm.6067-5.1011c0 2.3713-1.9223 4.2936-4.2936 4.2936C7.9223 14.5871 6 12.6648 6 10.2935 6 7.9223 7.9223 6 10.2935 6c2.3713 0 4.2936 1.9223 4.2936 4.2935z" fill-rule="evenodd">
        </path>
       </svg>
       <span class="hnf-btn__label">
        Rechercher
       </span>
      </span>
     </button>
    </div>
    <div class="hnf-menu__back hnf-menu__back--hidden">
     <button aria-expanded="true" aria-label="Revenir en arrière" class="hnf-btn hnf-btn--small hnf-btn--icon-tertiary" id="hnf-menu-back-btn" title="Revenir en arrière" type="button">
      <span class="hnf-btn__inner">
       <svg class="svg-icon hnf-svg-icon" fill="none" focusable="false" height="24" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
        <path clip-rule="evenodd" d="m3.999 11.9997 8 8.0011 1.4143-1.4141-5.5859-5.5866H20v-2H7.8273l5.5871-5.5868-1.4142-1.4143-8.0012 8.0007z" fill-rule="evenodd">
        </path>
       </svg>
      </span>
     </button>
    </div>
   </div>
   <div class="hnf-menu__container hnf-menu__container--pf hnf-menu__container--hidden">
    <nav aria-hidden="false" class="hnf-menu__nav">
     <ul class="hnf-menu__nav__main" data-main-links="">
      <li>
       <a class="hnf-link" data-index="0" data-tracking-label="" href="#" role="button">
        Des solutions abordables
       </a>
      </li>
      <li class="hnf-menu__nav__main__category hnf-menu__nav__main__category--first">
       <a class="hnf-link" data-index="c-0" data-tracking-label="fu001" href="https://www.ikea.com/ma/fr/cat/meubles-fu001/" role="button">
        Meubles
       </a>
      </li>
      <li class="hnf-menu__nav__main__category">
       <a class="hnf-link" data-index="c-1" data-tracking-label="ka001" href="https://www.ikea.com/ma/fr/cat/cuisine-et-electromenager-ka001/" role="button">
        Cuisine et électroménager
       </a>
      </li>
      <li class="hnf-menu__nav__main__category">
       <a class="hnf-link" data-index="c-2" data-tracking-label="bm001" href="https://www.ikea.com/ma/fr/cat/lits-et-matelas-bm001/" role="button">
        Lits et matelas
       </a>
      </li>
      <li class="hnf-menu__nav__main__category">
       <a class="hnf-link" data-index="c-3" data-tracking-label="st001" href="https://www.ikea.com/ma/fr/cat/rangement-st001/" role="button">
        Rangement
       </a>
      </li>
      <li class="hnf-menu__nav__main__category">
       <a class="hnf-link" data-index="c-4" data-tracking-label="700291" href="https://www.ikea.com/ma/fr/cat/travailler-de-la-maison-700291/" role="button">
        Travailler de la maison
       </a>
      </li>
      <li class="hnf-menu__nav__main__category">
       <a class="hnf-link" data-index="c-5" data-tracking-label="tl001" href="https://www.ikea.com/ma/fr/cat/linge-de-maison-et-textile-tl001/" role="button">
        Linge de maison et textile
       </a>
      </li>
      <li class="hnf-menu__nav__main__category">
       <a class="hnf-link" data-index="c-6" data-tracking-label="de001" href="https://www.ikea.com/ma/fr/cat/decoration-de001/" role="button">
        Décoration
       </a>
      </li>
      <li class="hnf-menu__nav__main__category">
       <a class="hnf-link" data-index="c-7" data-tracking-label="ba001" href="https://www.ikea.com/ma/fr/cat/salle-de-bain-ba001/" role="button">
        Salle de bain
       </a>
      </li>
      <li class="hnf-menu__nav__main__category">
       <a class="hnf-link" data-index="c-8" data-tracking-label="od001" href="https://www.ikea.com/ma/fr/cat/mobilier-et-accessoires-dexterieur-od001/" role="button">
        Mobilier et accessoires d'extérieur
       </a>
      </li>
      <li class="hnf-menu__nav__main__category">
       <a class="hnf-link" data-index="c-9" data-tracking-label="li001" href="https://www.ikea.com/ma/fr/cat/luminaires-et-eclairage-li001/" role="button">
        Luminaires et éclairage
       </a>
      </li>
      <li class="hnf-menu__nav__main__category">
       <a class="hnf-link" data-index="c-10" data-tracking-label="rm001" href="https://www.ikea.com/ma/fr/cat/tapis-et-paillasson-rm001/" role="button">
        Tapis et paillasson
       </a>
      </li>
      <li class="hnf-menu__nav__main__category">
       <a class="hnf-link" data-index="c-11" data-tracking-label="bc001" href="https://www.ikea.com/ma/fr/cat/bebe-et-enfant-bc001/" role="button">
        Bébé et enfant
       </a>
      </li>
      <li class="hnf-menu__nav__main__category">
       <a class="hnf-link" data-index="c-12" data-tracking-label="pp001" href="https://www.ikea.com/ma/fr/cat/plantes-cache-pots-et-supports-pp001/" role="button">
        Plantes, cache-pots et supports
       </a>
      </li>
      <li class="hnf-menu__nav__main__category">
       <a class="hnf-link" data-index="c-13" data-tracking-label="kt001" href="https://www.ikea.com/ma/fr/cat/arts-de-la-table-vaisselle-et-ustensiles-de-cuisine-kt001/" role="button">
        Arts de la table, vaisselle et ustensiles de cuisine
       </a>
      </li>
      <li class="hnf-menu__nav__main__category">
       <a class="hnf-link" data-index="c-14" data-tracking-label="ss001" href="https://www.ikea.com/ma/fr/cat/ete-ss001/" role="button">
        Été
       </a>
      </li>
      <li class="hnf-menu__nav__main__category">
       <a class="hnf-link" data-index="c-15" data-tracking-label="he001" href="https://www.ikea.com/ma/fr/cat/appareils-electroniques-he001/" role="button">
        Appareils électroniques
       </a>
      </li>
      <li class="hnf-menu__nav__main__category">
       <a class="hnf-link" data-index="c-16" data-tracking-label="lc001" href="https://www.ikea.com/ma/fr/cat/buanderie-lc001/" role="button">
        Buanderie
       </a>
      </li>
      <li class="hnf-menu__nav__main__category">
       <a class="hnf-link" data-index="c-17" data-tracking-label="hs001" href="https://www.ikea.com/ma/fr/cat/maison-connectee-hs001/" role="button">
        Maison connectée
       </a>
      </li>
      <li class="hnf-menu__nav__main__category">
       <a class="hnf-link" data-index="c-18" data-tracking-label="wt001" href="https://www.ikea.com/ma/fr/cat/noel-wt001/" role="button">
        Noël
       </a>
      </li>
      <li class="hnf-menu__nav__main__category">
       <a class="hnf-link" data-index="c-19" data-tracking-label="hi001" href="https://www.ikea.com/ma/fr/cat/personnalisation-et-entretien-hi001/" role="button">
        Personnalisation et entretien
       </a>
      </li>
      <li class="hnf-menu__nav__main__category hnf-menu__nav__main__category--last">
       <a class="hnf-link" data-index="c-20" data-tracking-label="fb001" href="https://www.ikea.com/ma/fr/cat/epicerie-suedoise-et-restauration-fb001/" role="button">
        Epicerie suédoise et Restauration
       </a>
      </li>
      <li>
       <a class="hnf-link" data-index="2" data-tracking-label="rooms" href="https://www.ikea.com/ma/fr/rooms/" role="button">
        Achetez par pièce
       </a>
      </li>
      <li>
       <a class="hnf-link" data-tracking-label="https://outlet.ikea.ma/ikeaoutlet/" href="https://outlet.ikea.ma/ikeaoutlet/">
        Outlet en ligne
       </a>
      </li>
      <li>
       <a class="hnf-link" data-index="4" data-tracking-label="" href="#" role="button">
        Bon à savoir
       </a>
      </li>
     </ul>
     <ul class="hnf-menu__nav__aux" data-aux-links="">
      <li>
       <a class="hnf-link" href="https://www.ikea.com/ma/fr/customer-service/">
        Service Clients
       </a>
      </li>
      <li>
       <a class="hnf-link" href="https://www.ikea.com/ma/fr/ikea-family/">
        IKEA Family
       </a>
      </li>
      <li>
       <a class="hnf-link" href="https://www.ikea.com/ma/fr/stores/">
        Boutique IKEA Maroc
       </a>
      </li>
      <li>
       <a class="hnf-link" href="https://www.ikea.com/ma/fr/stores/restaurant/">
        Restaurant IKEA
       </a>
      </li>
      <li>
       <a class="hnf-link" href="https://www.ikea.com/ma/en/this-is-ikea/">
        Voici IKEA
       </a>
      </li>
     </ul>
    </nav>
    <div class="hnf-menu__nav-wrapper">
     <div class="hnf-loading">
      <div aria-hidden="true" class="hnf-loading__ball-wrapper">
       <div class="hnf-loading__ball hnf-loading__ball--active">
       </div>
      </div>
     </div>
     <nav aria-hidden="true" class="hnf-menu__nav2 hnf-menu__nav2--hidden" data-index="0">
      <span class="hnf-menu__heading">
       Des solutions abordables
      </span>
      <ul aria-label="Sous-menu pour Des solutions abordables" class="hnf-menu__nav2__main" data-menu-sub2-links="" data-tracking-label="Des solutions abordables">
       <li>
        <a class="hnf-link" data-tracking-label="offers/lower-price" href="https://www.ikea.com/ma/fr/offers/lower-price/?filters=f-online-sellable%3Atrue">
         Prix encore plus bas
        </a>
       </li>
       <li>
        <a class="hnf-link" data-tracking-label="offers/lowest-price" href="https://www.ikea.com/ma/fr/offers/lowest-price/?filters=f-online-sellable%3Atrue&amp;sort=MOST_POPULAR">
         Le prix les plus bas
        </a>
       </li>
       <li>
        <a class="hnf-link" data-tracking-label="search/products" href="https://www.ikea.com/ma/fr/search/products/?group=l%27essentiel%20de%20la%20maison%20%C3%A0%20moins%20de%20100%20MAD&amp;sort=NAME_ASCENDING&amp;f-online-sellable=true#load-more-24">
         Essentiels à moins de 100DH
        </a>
       </li>
       <li>
        <a class="hnf-link" data-tracking-label="offers/best-sellers" href="https://www.ikea.com/ma/fr/offers/best-sellers/?sort=NAME_ASCENDING&amp;filters=f-online-sellable%3Atrue">
         Nos coups de cœur
        </a>
       </li>
      </ul>
     </nav>
     <nav aria-hidden="true" class="hnf-menu__nav2 hnf-menu__nav2--hidden" data-index="2">
      <span class="hnf-menu__heading">
       Achetez par pièce
      </span>
      <ul aria-label="Sous-menu pour Achetez par pièce" class="hnf-menu__nav2__main hnf-menu__nav2__main--rooms-grid" data-menu-sub2-links="" data-tracking-label="rooms">
       <li>
        <a class="rooms-grid-gap" data-tracking-label="rooms/bathroom" href="https://www.ikea.com/ma/fr/rooms/bathroom/">
         <span class="mr-aspect-ratio-image mr-aspect-ratio-image--wide">
          <img alt="Salle de bain" class="mr-aspect-ratio-image__image" data-src="https://www.ikea.com/images/salle-de-bain-de-style-contemporain-avec-carrelage-blanc-meu-b45d36fec556eeded02a8b052dbd0d9e.jpg?f=xxxs">
          </img>
         </span>
         <span class="mr__nav__title">
          Salle de bain
         </span>
        </a>
       </li>
       <li>
        <a class="rooms-grid-gap" data-tracking-label="rooms/bedroom" href="https://www.ikea.com/ma/fr/rooms/bedroom/">
         <span class="mr-aspect-ratio-image mr-aspect-ratio-image--wide">
          <img alt="Chambre" class="mr-aspect-ratio-image__image" data-src="https://www.ikea.com/images/dans-une-chambre-a-coucher-lit-matelasse-vadheim-avec-linge--18d599765b42ee3396abb67b8a245606.jpg?f=xxxs">
          </img>
         </span>
         <span class="mr__nav__title">
          Chambre
         </span>
        </a>
       </li>
       <li>
        <a class="rooms-grid-gap" data-tracking-label="rooms/childrens-room" href="https://www.ikea.com/ma/fr/rooms/childrens-room/">
         <span class="mr-aspect-ratio-image mr-aspect-ratio-image--wide">
          <img alt="Chambre bébé et enfant" class="mr-aspect-ratio-image__image" data-src="https://www.ikea.com/images/lits-superposes-tuffing-dans-une-chambre-denfant-ballon-de-f-57c6d97b0e97fa11316c8fea272a7f0d.jpg?f=xxxs"/>
         </span>
         <span class="mr__nav__title">
          Chambre bébé et enfant
         </span>
        </a>
       </li>
       <li>
        <a class="rooms-grid-gap" data-tracking-label="rooms/dining" href="https://www.ikea.com/ma/fr/rooms/dining/">
         <span class="mr-aspect-ratio-image mr-aspect-ratio-image--wide">
          <img alt="Salle à manger" class="mr-aspect-ratio-image__image" data-src="https://www.ikea.com/images/table-lisabo-noire-entouree-de-quatre-chaises-devant-des-bib-db20def55e23675a3157c8000ad834f1.jpg?f=xxxs"/>
         </span>
         <span class="mr__nav__title">
          Salle à manger
         </span>
        </a>
       </li>
       <li>
        <a class="rooms-grid-gap" data-tracking-label="rooms/hallway" href="https://www.ikea.com/ma/fr/rooms/hallway/">
         <span class="mr-aspect-ratio-image mr-aspect-ratio-image--wide">
          <img alt="Entrée" class="mr-aspect-ratio-image__image" data-src="https://www.ikea.com/images/hall-dentree-avec-armoire-penderie-platsa-a-portes-miroir-ba-f5db925bc4cdf3fcbd6d023c95aa7126.jpg?f=xxxs"/>
         </span>
         <span class="mr__nav__title">
          Entrée
         </span>
        </a>
       </li>
       <li>
        <a class="rooms-grid-gap" data-tracking-label="rooms/home-office" href="https://www.ikea.com/ma/fr/rooms/home-office/">
         <span class="mr-aspect-ratio-image mr-aspect-ratio-image--wide">
          <img alt="Bureau" class="mr-aspect-ratio-image__image" data-src="https://www.ikea.com/images/atelier-de-style-industriel-chez-un-particulier-plafonds-hau-d6ba3f797a6cbed87478bad1d8dbd652.jpg?f=xxxs"/>
         </span>
         <span class="mr__nav__title">
          Bureau
         </span>
        </a>
       </li>
       <li>
        <a class="rooms-grid-gap" data-tracking-label="rooms/kitchen" href="https://www.ikea.com/ma/fr/rooms/kitchen/">
         <span class="mr-aspect-ratio-image mr-aspect-ratio-image--wide">
          <img alt="Cuisine" class="mr-aspect-ratio-image__image" data-src="https://www.ikea.com/images/cuisine-contemporaine-bien-rangee-avec-facades-bodarp-gris-v-e83fe15f51c95aa7ccc4578fdffb3a4f.jpg?f=xxxs"/>
         </span>
         <span class="mr__nav__title">
          Cuisine
         </span>
        </a>
       </li>
       <li>
        <a class="rooms-grid-gap" data-tracking-label="rooms/living-room" href="https://www.ikea.com/ma/fr/rooms/living-room/">
         <span class="mr-aspect-ratio-image mr-aspect-ratio-image--wide">
          <img alt="Salon" class="mr-aspect-ratio-image__image" data-src="https://www.ikea.com/images/tables-gigognes-devant-un-canape-turquoise-clair-a-haut-doss-1109b1efb71d724410a031c1a2de4dfe.jpg?f=xxxs"/>
         </span>
         <span class="mr__nav__title">
          Salon
         </span>
        </a>
       </li>
       <li>
        <a class="rooms-grid-gap" data-tracking-label="rooms/outdoor" href="https://www.ikea.com/ma/fr/rooms/outdoor/">
         <span class="mr-aspect-ratio-image mr-aspect-ratio-image--wide">
          <img alt="Jardin, terrasse et balcon" class="mr-aspect-ratio-image__image" data-src="https://www.ikea.com/images/petit-balcon-avec-table-et-chaises-en-bois-gazon-artificiel--f6ba826dc19b000e2975955fd78e45a4.jpg?f=xxxs"/>
         </span>
         <span class="mr__nav__title">
          Jardin, terrasse et balcon
         </span>
        </a>
       </li>
       <li>
        <a class="rooms-grid-gap" data-tracking-label="ikea-business" href="https://www.ikea.com/ma/fr/ikea-business/">
         <span class="mr-aspect-ratio-image mr-aspect-ratio-image--wide">
          <img alt="Place d'affaires" class="mr-aspect-ratio-image__image" data-src="https://www.ikea.com/images/business-premises-with-sit-and-stand-desks-shelving-units-ch-78994382cd3bc3e6cd1df9ece58dfa35.jpg?f=xxxs"/>
         </span>
         <span class="mr__nav__title">
          Place d'affaires
         </span>
        </a>
       </li>
      </ul>
     </nav>
     <nav aria-hidden="true" class="hnf-menu__nav2 hnf-menu__nav2--hidden" data-index="4">
      <span class="hnf-menu__heading">
       Bon à savoir
      </span>
      <ul aria-label="Sous-menu pour Bon à savoir" class="hnf-menu__nav2__main" data-menu-sub2-links="" data-tracking-label="Bon à savoir">
       <li>
        <a class="hnf-link" data-tracking-label="ideas" href="https://www.ikea.com/ma/fr/ideas/">
         Inspiration &amp; idées
        </a>
       </li>
       <li>
        <a class="hnf-link" data-tracking-label="customer-service/returns-claims/guarantee" href="https://www.ikea.com/ma/fr/customer-service/returns-claims/guarantee/">
         Garanties et garanties
        </a>
       </li>
       <li>
        <a class="hnf-link" data-tracking-label="customer-service/returns-claims/return-policy" href="https://www.ikea.com/ma/fr/customer-service/returns-claims/return-policy/">
         Politique de retour de 90 jours
        </a>
       </li>
       <li>
        <a class="hnf-link" data-tracking-label="planners" href="https://www.ikea.com/ma/fr/planners/">
         Outils de planification
        </a>
       </li>
      </ul>
     </nav>
    </div>
   </div>
   <div class="hnf-menu__container hnf-menu__container--default hnf-menu__container--hidden">
    <nav aria-hidden="false" class="hnf-menu__nav">
     <ul class="hnf-menu__nav__main" data-main-links="">
      <li>
       <a class="hnf-link" data-index="0" data-tracking-label="" href="#" role="button">
        Des solutions abordables
       </a>
      </li>
      <li>
       <a class="hnf-link" data-index="1" data-products-link="" data-tracking-label="products" href="https://www.ikea.com/ma/fr/cat/products-products/" role="button">
        Produits
       </a>
      </li>
      <li>
       <a class="hnf-link" data-index="2" data-tracking-label="rooms" href="https://www.ikea.com/ma/fr/rooms/" role="button">
        Achetez par pièce
       </a>
      </li>
      <li>
       <a class="hnf-menu__nav__main--small hnf-link" data-tracking-label="https://outlet.ikea.ma/ikeaoutlet/" href="https://outlet.ikea.ma/ikeaoutlet/">
        Outlet en ligne
       </a>
      </li>
      <li>
       <a class="hnf-menu__nav__main--small hnf-link" data-index="4" data-tracking-label="" href="#" role="button">
        Bon à savoir
       </a>
      </li>
     </ul>
     <ul class="hnf-menu__nav__aux" data-aux-links="">
      <li>
       <a class="hnf-link" href="https://www.ikea.com/ma/fr/customer-service/">
        Service Clients
       </a>
      </li>
      <li>
       <a class="hnf-link" href="https://www.ikea.com/ma/fr/ikea-family/">
        IKEA Family
       </a>
      </li>
      <li>
       <a class="hnf-link" href="https://www.ikea.com/ma/fr/stores/">
        Boutique IKEA Maroc
       </a>
      </li>
      <li>
       <a class="hnf-link" href="https://www.ikea.com/ma/fr/stores/restaurant/">
        Restaurant IKEA
       </a>
      </li>
      <li>
       <a class="hnf-link" href="https://www.ikea.com/ma/en/this-is-ikea/">
        Voici IKEA
       </a>
      </li>
     </ul>
    </nav>
    <nav aria-hidden="true" class="hnf-menu__nav2 hnf-menu__nav2--hidden" data-index="0">
     <span class="hnf-menu__heading">
      Des solutions abordables
     </span>
     <ul aria-label="Sous-menu pour Des solutions abordables" class="hnf-menu__nav2__main" data-menu-sub3-links="" data-tracking-label="Des solutions abordables">
      <li>
       <a class="hnf-link" data-tracking-label="offers/lower-price" href="https://www.ikea.com/ma/fr/offers/lower-price/?filters=f-online-sellable%3Atrue">
        Prix encore plus bas
       </a>
      </li>
      <li>
       <a class="hnf-link" data-tracking-label="offers/lowest-price" href="https://www.ikea.com/ma/fr/offers/lowest-price/?filters=f-online-sellable%3Atrue&amp;sort=MOST_POPULAR">
        Le prix les plus bas
       </a>
      </li>
      <li>
       <a class="hnf-link" data-tracking-label="search/products" href="https://www.ikea.com/ma/fr/search/products/?group=l%27essentiel%20de%20la%20maison%20%C3%A0%20moins%20de%20100%20MAD&amp;sort=NAME_ASCENDING&amp;f-online-sellable=true#load-more-24">
        Essentiels à moins de 100DH
       </a>
      </li>
      <li>
       <a class="hnf-link" data-tracking-label="offers/best-sellers" href="https://www.ikea.com/ma/fr/offers/best-sellers/?sort=NAME_ASCENDING&amp;filters=f-online-sellable%3Atrue">
        Nos coups de cœur
       </a>
      </li>
     </ul>
    </nav>
    <nav aria-hidden="true" class="hnf-menu__nav2 hnf-menu__nav2--hidden" data-index="1">
     <span class="hnf-menu__heading">
      Produits
     </span>
     <ul aria-label="Sous-menu pour Produits" class="hnf-menu__nav2__main" data-menu-sub1-links="" data-show-rv="1" data-tracking-label="products">
      <li class="hnf-menu--highlight">
       <a class="hnf-link" data-tracking-label="new" href="https://www.ikea.com/ma/fr/new/">
        Nouveau
       </a>
      </li>
      <li class="hnf-menu--highlight">
       <a class="hnf-link" data-tracking-label="offers/last-chance" href="https://www.ikea.com/ma/fr/offers/last-chance/?filters=f-online-sellable%3Atrue">
        Dernière chance d'achat
       </a>
      </li>
     </ul>
     <div class="hnf-loading">
      <div aria-hidden="true" class="hnf-loading__ball-wrapper">
       <div class="hnf-loading__ball hnf-loading__ball--active">
       </div>
      </div>
      <a class="hnf-link" data-tracking-label="fu001" href="https://www.ikea.com/ma/fr/cat/meubles-fu001/">
       Meubles
      </a>
      <a class="hnf-link" data-tracking-label="ka001" href="https://www.ikea.com/ma/fr/cat/cuisine-et-electromenager-ka001/">
       Cuisine et électroménager
      </a>
      <a class="hnf-link" data-tracking-label="bm001" href="https://www.ikea.com/ma/fr/cat/lits-et-matelas-bm001/">
       Lits et matelas
      </a>
      <a class="hnf-link" data-tracking-label="st001" href="https://www.ikea.com/ma/fr/cat/rangement-st001/">
       Rangement
      </a>
      <a class="hnf-link" data-tracking-label="700291" href="https://www.ikea.com/ma/fr/cat/travailler-de-la-maison-700291/">
       Travailler de la maison
      </a>
      <a class="hnf-link" data-tracking-label="tl001" href="https://www.ikea.com/ma/fr/cat/linge-de-maison-et-textile-tl001/">
       Linge de maison et textile
      </a>
      <a class="hnf-link" data-tracking-label="de001" href="https://www.ikea.com/ma/fr/cat/decoration-de001/">
       Décoration
      </a>
      <a class="hnf-link" data-tracking-label="ba001" href="https://www.ikea.com/ma/fr/cat/salle-de-bain-ba001/">
       Salle de bain
      </a>
      <a class="hnf-link" data-tracking-label="od001" href="https://www.ikea.com/ma/fr/cat/mobilier-et-accessoires-dexterieur-od001/">
       Mobilier et accessoires d'extérieur
      </a>
      <a class="hnf-link" data-tracking-label="li001" href="https://www.ikea.com/ma/fr/cat/luminaires-et-eclairage-li001/">
       Luminaires et éclairage
      </a>
      <a class="hnf-link" data-tracking-label="rm001" href="https://www.ikea.com/ma/fr/cat/tapis-et-paillasson-rm001/">
       Tapis et paillasson
      </a>
      <a class="hnf-link" data-tracking-label="bc001" href="https://www.ikea.com/ma/fr/cat/bebe-et-enfant-bc001/">
       Bébé et enfant
      </a>
      <a class="hnf-link" data-tracking-label="pp001" href="https://www.ikea.com/ma/fr/cat/plantes-cache-pots-et-supports-pp001/">
       Plantes, cache-pots et supports
      </a>
      <a class="hnf-link" data-tracking-label="kt001" href="https://www.ikea.com/ma/fr/cat/arts-de-la-table-vaisselle-et-ustensiles-de-cuisine-kt001/">
       Arts de la table, vaisselle et ustensiles de cuisine
      </a>
      <a class="hnf-link" data-tracking-label="ss001" href="https://www.ikea.com/ma/fr/cat/ete-ss001/">
       Été
      </a>
      <a class="hnf-link" data-tracking-label="he001" href="https://www.ikea.com/ma/fr/cat/appareils-electroniques-he001/">
       Appareils électroniques
      </a>
      <a class="hnf-link" data-tracking-label="lc001" href="https://www.ikea.com/ma/fr/cat/buanderie-lc001/">
       Buanderie
      </a>
      <a class="hnf-link" data-tracking-label="hs001" href="https://www.ikea.com/ma/fr/cat/maison-connectee-hs001/">
       Maison connectée
      </a>
      <a class="hnf-link" data-tracking-label="wt001" href="https://www.ikea.com/ma/fr/cat/noel-wt001/">
       Noël
      </a>
      <a class="hnf-link" data-tracking-label="hi001" href="https://www.ikea.com/ma/fr/cat/personnalisation-et-entretien-hi001/">
       Personnalisation et entretien
      </a>
      <a class="hnf-link" data-tracking-label="fb001" href="https://www.ikea.com/ma/fr/cat/epicerie-suedoise-et-restauration-fb001/">
       Epicerie suédoise et Restauration
      </a>
     </div>
    </nav>
    <nav aria-hidden="true" class="hnf-menu__nav2 hnf-menu__nav2--hidden" data-index="2">
     <span class="hnf-menu__heading">
      Achetez par pièce
     </span>
     <ul aria-label="Sous-menu pour Achetez par pièce" class="hnf-menu__nav2__main hnf-menu__nav2__main--rooms-grid" data-menu-sub2-links="" data-tracking-label="rooms">
      <li>
       <a class="rooms-grid-gap" data-tracking-label="rooms/bathroom" href="https://www.ikea.com/ma/fr/rooms/bathroom/">
        <span class="mr-aspect-ratio-image mr-aspect-ratio-image--wide">
         <img alt="Salle de bain" class="mr-aspect-ratio-image__image" data-src="https://www.ikea.com/images/salle-de-bain-de-style-contemporain-avec-carrelage-blanc-meu-b45d36fec556eeded02a8b052dbd0d9e.jpg?f=xxxs"/>
        </span>
        <span class="mr__nav__title">
         Salle de bain
        </span>
       </a>
      </li>
      <li>
       <a class="rooms-grid-gap" data-tracking-label="rooms/bedroom" href="https://www.ikea.com/ma/fr/rooms/bedroom/">
        <span class="mr-aspect-ratio-image mr-aspect-ratio-image--wide">
         <img alt="Chambre" class="mr-aspect-ratio-image__image" data-src="https://www.ikea.com/images/dans-une-chambre-a-coucher-lit-matelasse-vadheim-avec-linge--18d599765b42ee3396abb67b8a245606.jpg?f=xxxs"/>
        </span>
        <span class="mr__nav__title">
         Chambre
        </span>
       </a>
      </li>
      <li>
       <a class="rooms-grid-gap" data-tracking-label="rooms/childrens-room" href="https://www.ikea.com/ma/fr/rooms/childrens-room/">
        <span class="mr-aspect-ratio-image mr-aspect-ratio-image--wide">
         <img alt="Chambre bébé et enfant" class="mr-aspect-ratio-image__image" data-src="https://www.ikea.com/images/lits-superposes-tuffing-dans-une-chambre-denfant-ballon-de-f-57c6d97b0e97fa11316c8fea272a7f0d.jpg?f=xxxs"/>
        </span>
        <span class="mr__nav__title">
         Chambre bébé et enfant
        </span>
       </a>
      </li>
      <li>
       <a class="rooms-grid-gap" data-tracking-label="rooms/dining" href="https://www.ikea.com/ma/fr/rooms/dining/">
        <span class="mr-aspect-ratio-image mr-aspect-ratio-image--wide">
         <img alt="Salle à manger" class="mr-aspect-ratio-image__image" data-src="https://www.ikea.com/images/table-lisabo-noire-entouree-de-quatre-chaises-devant-des-bib-db20def55e23675a3157c8000ad834f1.jpg?f=xxxs"/>
        </span>
        <span class="mr__nav__title">
         Salle à manger
        </span>
       </a>
      </li>
      <li>
       <a class="rooms-grid-gap" data-tracking-label="rooms/hallway" href="https://www.ikea.com/ma/fr/rooms/hallway/">
        <span class="mr-aspect-ratio-image mr-aspect-ratio-image--wide">
         <img alt="Entrée" class="mr-aspect-ratio-image__image" data-src="https://www.ikea.com/images/hall-dentree-avec-armoire-penderie-platsa-a-portes-miroir-ba-f5db925bc4cdf3fcbd6d023c95aa7126.jpg?f=xxxs"/>
        </span>
        <span class="mr__nav__title">
         Entrée
        </span>
       </a>
      </li>
      <li>
       <a class="rooms-grid-gap" data-tracking-label="rooms/home-office" href="https://www.ikea.com/ma/fr/rooms/home-office/">
        <span class="mr-aspect-ratio-image mr-aspect-ratio-image--wide">
         <img alt="Bureau" class="mr-aspect-ratio-image__image" data-src="https://www.ikea.com/images/atelier-de-style-industriel-chez-un-particulier-plafonds-hau-d6ba3f797a6cbed87478bad1d8dbd652.jpg?f=xxxs"/>
        </span>
        <span class="mr__nav__title">
         Bureau
        </span>
       </a>
      </li>
      <li>
       <a class="rooms-grid-gap" data-tracking-label="rooms/kitchen" href="https://www.ikea.com/ma/fr/rooms/kitchen/">
        <span class="mr-aspect-ratio-image mr-aspect-ratio-image--wide">
         <img alt="Cuisine" class="mr-aspect-ratio-image__image" data-src="https://www.ikea.com/images/cuisine-contemporaine-bien-rangee-avec-facades-bodarp-gris-v-e83fe15f51c95aa7ccc4578fdffb3a4f.jpg?f=xxxs"/>
        </span>
        <span class="mr__nav__title">
         Cuisine
        </span>
       </a>
      </li>
      <li>
       <a class="rooms-grid-gap" data-tracking-label="rooms/living-room" href="https://www.ikea.com/ma/fr/rooms/living-room/">
        <span class="mr-aspect-ratio-image mr-aspect-ratio-image--wide">
         <img alt="Salon" class="mr-aspect-ratio-image__image" data-src="https://www.ikea.com/images/tables-gigognes-devant-un-canape-turquoise-clair-a-haut-doss-1109b1efb71d724410a031c1a2de4dfe.jpg?f=xxxs"/>
        </span>
        <span class="mr__nav__title">
         Salon
        </span>
       </a>
      </li>
      <li>
       <a class="rooms-grid-gap" data-tracking-label="rooms/outdoor" href="https://www.ikea.com/ma/fr/rooms/outdoor/">
        <span class="mr-aspect-ratio-image mr-aspect-ratio-image--wide">
         <img alt="Jardin, terrasse et balcon" class="mr-aspect-ratio-image__image" data-src="https://www.ikea.com/images/petit-balcon-avec-table-et-chaises-en-bois-gazon-artificiel--f6ba826dc19b000e2975955fd78e45a4.jpg?f=xxxs"/>
        </span>
        <span class="mr__nav__title">
         Jardin, terrasse et balcon
        </span>
       </a>
      </li>
      <li>
       <a class="rooms-grid-gap" data-tracking-label="ikea-business" href="https://www.ikea.com/ma/fr/ikea-business/">
        <span class="mr-aspect-ratio-image mr-aspect-ratio-image--wide">
         <img alt="Place d'affaires" class="mr-aspect-ratio-image__image" data-src="https://www.ikea.com/images/business-premises-with-sit-and-stand-desks-shelving-units-ch-78994382cd3bc3e6cd1df9ece58dfa35.jpg?f=xxxs"/>
        </span>
        <span class="mr__nav__title">
         Place d'affaires
        </span>
       </a>
      </li>
     </ul>
    </nav>
    <nav aria-hidden="true" class="hnf-menu__nav2 hnf-menu__nav2--hidden" data-index="4">
     <span class="hnf-menu__heading">
      Bon à savoir
     </span>
     <ul aria-label="Sous-menu pour Bon à savoir" class="hnf-menu__nav2__main" data-menu-sub3-links="" data-tracking-label="Bon à savoir">
      <li>
       <a class="hnf-link" data-tracking-label="ideas" href="https://www.ikea.com/ma/fr/ideas/">
        Inspiration &amp; idées
       </a>
      </li>
      <li>
       <a class="hnf-link" data-tracking-label="customer-service/returns-claims/guarantee" href="https://www.ikea.com/ma/fr/customer-service/returns-claims/guarantee/">
        Garanties et garanties
       </a>
      </li>
      <li>
       <a class="hnf-link" data-tracking-label="customer-service/returns-claims/return-policy" href="https://www.ikea.com/ma/fr/customer-service/returns-claims/return-policy/">
        Politique de retour de 90 jours
       </a>
      </li>
      <li>
       <a class="hnf-link" data-tracking-label="planners" href="https://www.ikea.com/ma/fr/planners/">
        Outils de planification
       </a>
      </li>
     </ul>
    </nav>
    <div aria-hidden="true" class="hnf-menu__rv hnf-menu__rv--hidden">
     <span class="hnf-menu__rv__heading">
      Récemment consulté
     </span>
     <div class="hnf-menu__rv__list">
     </div>
    </div>
   </div>
   <div class="hnf-menu__alternate">
    <div class="hnf-quantity-dropdown hnf-switch-language">
     <select aria-label="Sélectionnez votre langue préférée">
      <option value="https://www.ikea.com/ma/fr/">
       Français
      </option>
      <option value="https://www.ikea.com/ma/ar/">
       العربية
      </option>
      <option value="https://www.ikea.com/ma/en/">
       English
      </option>
     </select>
     <svg class="svg-icon hnf-svg-icon hnf-svg-icon--100 hnf-quantity-dropdown__chevron" fill="none" focusable="false" height="24" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
      <path clip-rule="evenodd" d="M11.9999 17.0605 3.9992 9.0593l1.4142-1.4141L12 14.2322l6.5869-6.586 1.4141 1.4143-8.0011 8z" fill-rule="evenodd">
      </path>
     </svg>
    </div>
    <a class="hnf-link hnf-btn hnf-btn-change-country" href="https://www.ikea.com">
     <svg class="svg-icon hnf-svg-icon hnf-btn-change-country__globe" fill="none" focusable="false" height="24" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
      <path clip-rule="evenodd" d="M13.7467 18.1766C12.9482 19.7737 12.2151 20 12 20c-.2151 0-.9482-.2263-1.7467-1.8234-.3065-.6131-.5745-1.3473-.7831-2.1766h5.0596c-.2086.8293-.4766 1.5635-.7831 2.1766zM14.8885 14h-5.777A17.7354 17.7354 0 0 1 9 12c0-.6949.0392-1.3641.1115-2h5.777c.0723.6359.1115 1.3051.1115 2 0 .6949-.0392 1.3641-.1115 2zm1.6955 2c-.2658 1.2166-.6492 2.307-1.1213 3.2138A8.0347 8.0347 0 0 0 18.9297 16H16.584zm3.164-2H16.9c.0656-.6462.1-1.3151.1-2 0-.6849-.0344-1.3538-.1-2h2.848A8.0156 8.0156 0 0 1 20 12a8.0156 8.0156 0 0 1-.252 2zm-.8183-6a8.035 8.035 0 0 0-3.467-3.2138c.4721.9068.8555 1.9972 1.1213 3.2138h2.3457zm-4.3999 0c-.2086-.8293-.4766-1.5635-.7831-2.1766C12.9482 4.2264 12.2151 4 12 4c-.2151 0-.9482.2263-1.7467 1.8234-.3065.613-.5745 1.3473-.7831 2.1766h5.0596zM7.416 8c.2658-1.2166.6491-2.307 1.1213-3.2138A8.035 8.035 0 0 0 5.0703 8H7.416zm-3.164 2A8.0147 8.0147 0 0 0 4 12c0 .6906.0875 1.3608.252 2H7.1a19.829 19.829 0 0 1-.1-2c0-.6849.0344-1.3538.1-2H4.252zm3.164 6H5.0704a8.0347 8.0347 0 0 0 3.467 3.2138C8.0651 18.307 7.6818 17.2166 7.4161 16zM22 12c0-5.5229-4.4772-10-10-10C6.4771 2 2 6.4771 2 12c0 5.5228 4.4771 10 10 10 5.5228 0 10-4.4772 10-10z" fill-rule="evenodd">
      </path>
     </svg>
     Changer de pays
    </a>
   </div>
  </aside>
  <div class="hnf-overlay">
  </div>
  <div id="hnf-content" tabindex="-1">
  </div>
  <script id="plp-page-meta-data" type="application/json">
   {"correctUrl":"/ma/fr/cat/meubles-fu001/"}
  </script>
  <div class="plp-page-container">
   <div class="plp-page-container__inner">
    <div class="plp-page-container__main">
     <a class="plp-skip-to-product-list" href="#product-list-skip">
      Passer à la liste des produits
     </a>
     <div class="bc-breadcrumb bc-breadcrumb--short">
      <nav aria-label="Breadcrumb" class="bc-breadcrumb__nav" role="navigation">
       <ol class="bc-breadcrumb__list" data-breadcrumb-links="">
        <li class="bc-breadcrumb__list-item">
         <a class="bc-breadcrumb__link bc-link bc-link--black" data-tracking-label="products" href="https://www.ikea.com/ma/fr/cat/produits-products/">
          <span>
           Produits
          </span>
         </a>
        </li>
        <li class="bc-breadcrumb__list-item">
         <a class="bc-breadcrumb__link bc-link bc-link--black" data-tracking-label="products | fu001" href="https://www.ikea.com/ma/fr/cat/meubles-fu001/">
          <span>
           Meubles
          </span>
         </a>
        </li>
       </ol>
      </nav>
     </div>
     <div aria-hidden="false" class="hnf-inline-message hnf-inline-message--informative" id="hnf-page-message">
      <div>
       <span class="hnf-inline-message__text">
        <a class="hnf-link" data-page-message-link="" href="https://www.ikea.com/ma/fr/offers/lower-price/?filters=f-online-sellable%3Atrue">
         Découvrez nos solutions à prix encore plus bas sans plus tarder
        </a>
       </span>
      </div>
     </div>
     <script type="application/ld+json">
      {
  "@context":"https://schema.org",
  "@type":"BreadcrumbList",
  "itemListElement": [
     {
         "@type" : "ListItem", "position": 1, "name": "Produits", "item": "https://www.ikea.com/ma/fr/cat/produits-products/"
     },
     {
         "@type" : "ListItem", "position": 2, "name": "Meubles", "item": "https://www.ikea.com/ma/fr/cat/meubles-fu001/"
     }
     
     
  ]
}
     </script>
     <div class="plp-page-title">
      <h1 class="plp-page-title__title">
       Meubles
      </h1>
     </div>
     <div class="plp-navigation-slot-wrapper">
      <div class="vn-carousel">
       <div class="vn__wrapper">
        <nav class="vn__nav vn-6-grid" data-visual-navigation-links="" role="navigation">
         <a class="vn-link vn__nav__link vn-6-grid-gap" data-tracking-label="products | fu001 | 55002" href="https://www.ikea.com/ma/fr/cat/meubles-de-gaming-55002/">
          <span class="vn-aspect-ratio-image vn-aspect-ratio-image--wide">
           <img alt="Meubles de gaming" class="vn-aspect-ratio-image__image" loading="lazy" src="https://www.ikea.com/global/assets/navigation/images/gaming-furniture-55002.jpeg?imwidth=300"/>
          </span>
          <span aria-hidden="true" class="vn__nav__title">
           Meubles de gaming
          </span>
         </a>
         <a class="vn-link vn__nav__link vn-6-grid-gap" data-tracking-label="products | fu001 | 55036" href="https://www.ikea.com/ma/fr/cat/ensembles-de-meubles-55036/">
          <span class="vn-aspect-ratio-image vn-aspect-ratio-image--wide">
           <img alt="Ensembles de meubles" class="vn-aspect-ratio-image__image" loading="lazy" src="https://www.ikea.com/global/assets/navigation/images/furniture-sets-55036.jpeg?imwidth=300"/>
          </span>
          <span aria-hidden="true" class="vn__nav__title">
           Ensembles de meubles
          </span>
         </a>
         <a class="vn-link vn__nav__link vn-6-grid-gap" data-tracking-label="products | fu001 | bm003" href="https://www.ikea.com/ma/fr/cat/lits-bm003/">
          <span class="vn-aspect-ratio-image vn-aspect-ratio-image--wide">
           <img alt="Lits" class="vn-aspect-ratio-image__image" loading="lazy" src="https://www.ikea.com/global/assets/navigation/images/beds-bm003.jpeg?imwidth=300"/>
          </span>
          <span aria-hidden="true" class="vn__nav__title">
           Lits
          </span>
         </a>
         <a class="vn-link vn__nav__link vn-6-grid-gap" data-tracking-label="products | fu001 | fu003" href="https://www.ikea.com/ma/fr/cat/canapes-fu003/">
          <span class="vn-aspect-ratio-image vn-aspect-ratio-image--wide">
           <img alt="Canapés" class="vn-aspect-ratio-image__image" loading="lazy" src="https://www.ikea.com/global/assets/navigation/images/sofas-fu003.jpeg?imwidth=300"/>
          </span>
          <span aria-hidden="true" class="vn__nav__title">
           Canapés
          </span>
         </a>
         <a class="vn-link vn__nav__link vn-6-grid-gap" data-tracking-label="products | fu001 | st002" href="https://www.ikea.com/ma/fr/cat/bibliotheques-et-etageres-st002/">
          <span class="vn-aspect-ratio-image vn-aspect-ratio-image--wide">
           <img alt="Bibliothèques et étagères" class="vn-aspect-ratio-image__image" loading="lazy" src="https://www.ikea.com/global/assets/navigation/images/bookcases-shelving-units-st002.jpeg?imwidth=300"/>
          </span>
          <span aria-hidden="true" class="vn__nav__title">
           Bibliothèques et étagères
          </span>
         </a>
         <a class="vn-link vn__nav__link vn-6-grid-gap" data-tracking-label="products | fu001 | fu004" href="https://www.ikea.com/ma/fr/cat/tables-et-bureaux-fu004/">
          <span class="vn-aspect-ratio-image vn-aspect-ratio-image--wide">
           <img alt="Tables et bureaux" class="vn-aspect-ratio-image__image" loading="lazy" src="https://www.ikea.com/global/assets/navigation/images/tables-desks-fu004.jpeg?imwidth=300"/>
          </span>
          <span aria-hidden="true" class="vn__nav__title">
           Tables et bureaux
          </span>
         </a>
         <a class="vn-link vn__nav__link vn-6-grid-gap" data-tracking-label="products | fu001 | st003" href="https://www.ikea.com/ma/fr/cat/rangements-bureau-et-salon-st003/">
          <span class="vn-aspect-ratio-image vn-aspect-ratio-image--wide">
           <img alt="Rangements bureau et salon" class="vn-aspect-ratio-image__image" loading="lazy" src="https://www.ikea.com/global/assets/navigation/images/cabinets-cupboards-st003.jpeg?imwidth=300"/>
          </span>
          <span aria-hidden="true" class="vn__nav__title">
           Rangements bureau et salon
          </span>
         </a>
         <a class="vn-link vn__nav__link vn-6-grid-gap" data-tracking-label="products | fu001 | 10475" href="https://www.ikea.com/ma/fr/cat/meubles-tv-10475/">
          <span class="vn-aspect-ratio-image vn-aspect-ratio-image--wide">
           <img alt="Meubles TV" class="vn-aspect-ratio-image__image" loading="lazy" src="https://www.ikea.com/global/assets/navigation/images/tv-media-furniture-10475.jpeg?imwidth=300"/>
          </span>
          <span aria-hidden="true" class="vn__nav__title">
           Meubles TV
          </span>
         </a>
         <a class="vn-link vn__nav__link vn-6-grid-gap" data-tracking-label="products | fu001 | st004" href="https://www.ikea.com/ma/fr/cat/commodes-et-caissons-a-tiroirs-st004/">
          <span class="vn-aspect-ratio-image vn-aspect-ratio-image--wide">
           <img alt="Commodes et caissons à tiroirs" class="vn-aspect-ratio-image__image" loading="lazy" src="https://www.ikea.com/global/assets/navigation/images/chests-of-drawers-drawer-units-st004.jpeg?imwidth=300"/>
          </span>
          <span aria-hidden="true" class="vn__nav__title">
           Commodes et caissons à tiroirs
          </span>
         </a>
         <a class="vn-link vn__nav__link vn-6-grid-gap" data-tracking-label="products | fu001 | 19053" href="https://www.ikea.com/ma/fr/cat/armoires-penderies-et-dressings-19053/">
          <span class="vn-aspect-ratio-image vn-aspect-ratio-image--wide">
           <img alt="Armoires, penderies et dressings" class="vn-aspect-ratio-image__image" loading="lazy" src="https://www.ikea.com/global/assets/navigation/images/wardrobes-19053.jpeg?imwidth=300"/>
          </span>
          <span aria-hidden="true" class="vn__nav__title">
           Armoires, penderies et dressings
          </span>
         </a>
         <a class="vn-link vn__nav__link vn-6-grid-gap" data-tracking-label="products | fu001 | fu002" href="https://www.ikea.com/ma/fr/cat/chaises-fu002/">
          <span class="vn-aspect-ratio-image vn-aspect-ratio-image--wide">
           <img alt="Chaises" class="vn-aspect-ratio-image__image" loading="lazy" src="https://www.ikea.com/global/assets/navigation/images/chairs-fu002.jpeg?imwidth=300"/>
          </span>
          <span aria-hidden="true" class="vn__nav__title">
           Chaises
          </span>
         </a>
         <a class="vn-link vn__nav__link vn-6-grid-gap" data-tracking-label="products | fu001 | od003" href="https://www.ikea.com/ma/fr/cat/mobilier-de-jardin-od003/">
          <span class="vn-aspect-ratio-image vn-aspect-ratio-image--wide">
           <img alt="Mobilier de jardin" class="vn-aspect-ratio-image__image" loading="lazy" src="https://www.ikea.com/global/assets/navigation/images/outdoor-furniture-od003.jpeg?imwidth=300"/>
          </span>
          <span aria-hidden="true" class="vn__nav__title">
           Mobilier de jardin
          </span>
         </a>
         <a class="vn-link vn__nav__link vn-6-grid-gap" data-tracking-label="products | fu001 | 30454" href="https://www.ikea.com/ma/fr/cat/buffets-et-consoles-30454/">
          <span class="vn-aspect-ratio-image vn-aspect-ratio-image--wide">
           <img alt="Buffets et consoles" class="vn-aspect-ratio-image__image" loading="lazy" src="https://www.ikea.com/global/assets/navigation/images/sideboards-buffets-console-tables-30454.jpeg?imwidth=300"/>
          </span>
          <span aria-hidden="true" class="vn__nav__title">
           Buffets et consoles
          </span>
         </a>
         <a class="vn-link vn__nav__link vn-6-grid-gap" data-tracking-label="products | fu001 | 18767" href="https://www.ikea.com/ma/fr/cat/meubles-enfant-18767/">
          <span class="vn-aspect-ratio-image vn-aspect-ratio-image--wide">
           <img alt="Meubles enfant" class="vn-aspect-ratio-image__image" loading="lazy" src="https://www.ikea.com/global/assets/navigation/images/childrens-furniture-18767.jpeg?imwidth=300"/>
          </span>
          <span aria-hidden="true" class="vn__nav__title">
           Meubles enfant
          </span>
         </a>
         <a class="vn-link vn__nav__link vn-6-grid-gap" data-tracking-label="products | fu001 | 46080" href="https://www.ikea.com/ma/fr/cat/separateurs-de-piece-46080/">
          <span class="vn-aspect-ratio-image vn-aspect-ratio-image--wide">
           <img alt="Séparateurs de pièce" class="vn-aspect-ratio-image__image" loading="lazy" src="https://www.ikea.com/global/assets/navigation/images/room-dividers-46080.jpeg?imwidth=300"/>
          </span>
          <span aria-hidden="true" class="vn__nav__title">
           Séparateurs de pièce
          </span>
         </a>
         <a class="vn-link vn__nav__link vn-6-grid-gap" data-tracking-label="products | fu001 | fu005" href="https://www.ikea.com/ma/fr/cat/dessertes-et-ilots-fu005/">
          <span class="vn-aspect-ratio-image vn-aspect-ratio-image--wide">
           <img alt="Dessertes et îlots" class="vn-aspect-ratio-image__image" loading="lazy" src="https://www.ikea.com/global/assets/navigation/images/trolleys-fu005.jpeg?imwidth=300"/>
          </span>
          <span aria-hidden="true" class="vn__nav__title">
           Dessertes et îlots
          </span>
         </a>
         <a class="vn-link vn__nav__link vn-6-grid-gap" data-tracking-label="products | fu001 | 16244" href="https://www.ikea.com/ma/fr/cat/tables-et-chaises-de-bar-16244/">
          <span class="vn-aspect-ratio-image vn-aspect-ratio-image--wide">
           <img alt="Tables et chaises de bar" class="vn-aspect-ratio-image__image" loading="lazy" src="https://www.ikea.com/global/assets/navigation/images/bar-furniture-16244.jpeg?imwidth=300"/>
          </span>
          <span aria-hidden="true" class="vn__nav__title">
           Tables et chaises de bar
          </span>
         </a>
         <a class="vn-link vn__nav__link vn-6-grid-gap" data-tracking-label="products | fu001 | fu006" href="https://www.ikea.com/ma/fr/cat/fauteuils-et-meridiennes-fu006/">
          <span class="vn-aspect-ratio-image vn-aspect-ratio-image--wide">
           <img alt="Fauteuils et méridiennes" class="vn-aspect-ratio-image__image" loading="lazy" src="https://www.ikea.com/global/assets/navigation/images/armchairs-chaise-longues-fu006.jpeg?imwidth=300"/>
          </span>
          <span aria-hidden="true" class="vn__nav__title">
           Fauteuils et méridiennes
          </span>
         </a>
         <a class="vn-link vn__nav__link vn-6-grid-gap" data-tracking-label="products | fu001 | 19141" href="https://www.ikea.com/ma/fr/cat/mobilier-de-cafe-et-restaurant-19141/">
          <span class="vn-aspect-ratio-image vn-aspect-ratio-image--wide">
           <img alt="Mobilier de café et restaurant" class="vn-aspect-ratio-image__image" loading="lazy" src="https://www.ikea.com/global/assets/navigation/images/cafe-furniture-19141.jpeg?imwidth=300"/>
          </span>
          <span aria-hidden="true" class="vn__nav__title">
           Mobilier de café et restaurant
          </span>
         </a>
         <a class="vn-link vn__nav__link vn-6-grid-gap" data-tracking-label="products | fu001 | 45780" href="https://www.ikea.com/ma/fr/cat/meubles-bebe-45780/">
          <span class="vn-aspect-ratio-image vn-aspect-ratio-image--wide">
           <img alt="Meubles bébé" class="vn-aspect-ratio-image__image" loading="lazy" src="https://www.ikea.com/global/assets/navigation/images/nursery-furniture-45780.jpeg?imwidth=300"/>
          </span>
          <span aria-hidden="true" class="vn__nav__title">
           Meubles bébé
          </span>
         </a>
        </nav>
       </div>
       <div class="vn-scroll-indicator">
        <div class="vn-scroll-indicator__bar" style="transform: scaleX(0.25) translateX(0%);" tabindex="0">
        </div>
       </div>
      </div>
     </div>
     <div class="plp-various-content-slot-wrapper" data-collapsible="false" data-range-slot="various-content">
      <div class="pub__designSystemBase" data-pub-ga="">
       <div class="gd8xc1c v1gpv7o0 v18by0fb">
        <section class="gd8xc1c v19w64p3 v18by0fb">
         <div id="b92345c0-2028-11ec-a94b-dd6dc2fa4f6e">
          <div class="r5llg8g" data-pub-id="b92345c0-2028-11ec-a94b-dd6dc2fa4f6e" data-pub-type="image-with-text-box">
           <div class="gd8xc1c v11tpn0s v18by0fb">
            <h2 class="c1m1sl8e pub__h2 s1gshh7t">
             Vous manquez de place? Faites preuve de créativité.
            </h2>
            <div class="h1mnt178">
             <span class="pub__aspect-ratio-image pub__aspect-ratio-image--portrait-to-wide-from-md">
              <img alt="Voir toutes nos bibliothèques et étagères." class="pub__aspect-ratio-image__image" loading="lazy" sizes="(min-width: 56.25em) 78vw, 100vw" src="https://www.ikea.com/images/voir-toutes-nos-bibliotheques-et-etageres-1c50b9ff30b8e5277e3410b1248e2975.jpg?f=s" srcset="https://www.ikea.com/images/voir-toutes-nos-bibliotheques-et-etageres-1c50b9ff30b8e5277e3410b1248e2975.jpg?f=sg 1600w,
  https://www.ikea.com/images/voir-toutes-nos-bibliotheques-et-etageres-1c50b9ff30b8e5277e3410b1248e2975.jpg?f=xxxl 1400w,
  https://www.ikea.com/images/voir-toutes-nos-bibliotheques-et-etageres-1c50b9ff30b8e5277e3410b1248e2975.jpg?f=xxl 950w,
  https://www.ikea.com/images/voir-toutes-nos-bibliotheques-et-etageres-1c50b9ff30b8e5277e3410b1248e2975.jpg?f=xl 800w,
  https://www.ikea.com/images/voir-toutes-nos-bibliotheques-et-etageres-1c50b9ff30b8e5277e3410b1248e2975.jpg?f=l 750w,
  https://www.ikea.com/images/voir-toutes-nos-bibliotheques-et-etageres-1c50b9ff30b8e5277e3410b1248e2975.jpg?f=m 600w,
  https://www.ikea.com/images/voir-toutes-nos-bibliotheques-et-etageres-1c50b9ff30b8e5277e3410b1248e2975.jpg?f=s 500w,
  https://www.ikea.com/images/voir-toutes-nos-bibliotheques-et-etageres-1c50b9ff30b8e5277e3410b1248e2975.jpg?f=xs 400w,
  https://www.ikea.com/images/voir-toutes-nos-bibliotheques-et-etageres-1c50b9ff30b8e5277e3410b1248e2975.jpg?f=xxs 300w,
  https://www.ikea.com/images/voir-toutes-nos-bibliotheques-et-etageres-1c50b9ff30b8e5277e3410b1248e2975.jpg?f=xxxs 240w"/>
             </span>
             <div class="b1nwnxkd nklljlt">
              <a class="b1cw4fo1 ddaom9 pub__link pub__link--black" href="https://www.ikea.com/ma/fr/cat/bibliotheques-et-etageres-st002/">
               <span class="i16crrbz">
                <span>
                 <p class="n1lc5xb3 pub__h4 s1gshh7t">
                  Voir toutes les bibliothèques et étagères
                 </p>
                </span>
                <svg aria-hidden="true" class="pub__svg-icon i1661flk" focusable="false" viewbox="0 0 24 24">
                 <path clip-rule="evenodd" d="M19.2937 12.7074L20.0008 12.0003L19.2938 11.2932L12.0008 3.99927L10.5865 5.41339L16.1727 11.0003H4V13.0003H16.1723L10.5855 18.5868L11.9996 20.0011L19.2937 12.7074Z" fill-rule="evenodd">
                 </path>
                </svg>
               </span>
              </a>
             </div>
             <div class="n1xbvpiu">
              <a class="c18acreo pub__link" href="https://www.ikea.com/ma/fr/cat/bibliotheques-et-etageres-st002/">
               <span>
                <p class="n1lc5xb3 pub__h4 s1gshh7t">
                 Voir toutes les bibliothèques et étagères
                </p>
               </span>
               <svg aria-hidden="true" class="pub__svg-icon" focusable="false" viewbox="0 0 24 24">
                <path clip-rule="evenodd" d="m15.5996 12.0007-5.785 5.7857-1.4143-1.4141 4.3711-4.3716L8.4003 7.629l1.4143-1.4142 5.785 5.7859z" fill-rule="evenodd">
                </path>
               </svg>
              </a>
             </div>
            </div>
           </div>
          </div>
         </div>
        </section>
        <section class="gd8xc1c v19w64p3 v18by0fb">
         <div id="16bf8180-2029-11ec-a94b-dd6dc2fa4f6e">
          <div class="c1lpg3h5 i1ycpxq9 pub__designSystemText t91kxqv w1fdzi2f" data-pub-id="16bf8180-2029-11ec-a94b-dd6dc2fa4f6e" data-pub-type="text">
           <h2>
            Armoires-penderies pour petits et grands espaces
           </h2>
          </div>
         </div>
         <div id="10ecdff0-2029-11ec-a94b-dd6dc2fa4f6e">
          <div data-pub-id="10ecdff0-2029-11ec-a94b-dd6dc2fa4f6e" data-pub-type="container">
           <div class="cmmh5q7 xbcjakg mj54kgs l1twdhvz x1aacaiq m1l3ov8s mfmjk3b mqpv3tm mw61hmb mc0hq6s s1vteuqm">
            <div class="s1cmcu6f">
             <div class="gd8xc1c vz2frqh v18by0fb">
              <div id="20ab7be0-2029-11ec-a94b-dd6dc2fa4f6e">
               <figure class="gd8xc1c v1tibsle gqfus6o v18by0fb" data-pub-id="20ab7be0-2029-11ec-a94b-dd6dc2fa4f6e" data-pub-type="image-with-caption" role="group">
                <div>
                 <pub-hide-empty-link>
                  <a class="b1cw4fo1 pub__link pub__link--black" href="https://www.ikea.com/ma/fr/cat/platsa-systeme-37894/">
                   <div class="g5qtjc5 gxo7hqh h1f0e657 r5llg8g" style="height:auto;padding-bottom:56.2%;padding-left:0">
                    <div class="i1llvon7">
                     <img alt="Système PLATSA." loading="lazy" onerror="this.onerror=null; const parent = this.closest('div'); parent.classList.add('e6qunvq')" sizes="(min-width: 56.25em) 25vw, (min-width: 37.5em) 40vw, 90vw" src="https://www.ikea.com/images/systeme-platsa-1a626ef41ab7c5bb2417dd79ee241876.jpg?f=s" srcset="https://www.ikea.com/images/systeme-platsa-1a626ef41ab7c5bb2417dd79ee241876.jpg?f=sg 1600w,
  https://www.ikea.com/images/systeme-platsa-1a626ef41ab7c5bb2417dd79ee241876.jpg?f=xxxl 1400w,
  https://www.ikea.com/images/systeme-platsa-1a626ef41ab7c5bb2417dd79ee241876.jpg?f=xxl 950w,
  https://www.ikea.com/images/systeme-platsa-1a626ef41ab7c5bb2417dd79ee241876.jpg?f=xl 800w,
  https://www.ikea.com/images/systeme-platsa-1a626ef41ab7c5bb2417dd79ee241876.jpg?f=l 750w,
  https://www.ikea.com/images/systeme-platsa-1a626ef41ab7c5bb2417dd79ee241876.jpg?f=m 600w,
  https://www.ikea.com/images/systeme-platsa-1a626ef41ab7c5bb2417dd79ee241876.jpg?f=s 500w,
  https://www.ikea.com/images/systeme-platsa-1a626ef41ab7c5bb2417dd79ee241876.jpg?f=xs 400w,
  https://www.ikea.com/images/systeme-platsa-1a626ef41ab7c5bb2417dd79ee241876.jpg?f=xxs 300w,
  https://www.ikea.com/images/systeme-platsa-1a626ef41ab7c5bb2417dd79ee241876.jpg?f=xxxs 240w"/>
                    </div>
                   </div>
                  </a>
                 </pub-hide-empty-link>
                </div>
                <figcaption class="i1ycpxq9 pub__designSystemText t91kxqv">
                 Système PLATSA – rangements flexibles et modulaires pour exploiter l’espace au maximum
                </figcaption>
               </figure>
              </div>
             </div>
            </div>
            <div class="s1cmcu6f">
             <div class="gd8xc1c vz2frqh v18by0fb">
              <div id="21a2fb40-2029-11ec-a94b-dd6dc2fa4f6e">
               <figure class="gd8xc1c v1tibsle gqfus6o v18by0fb" data-pub-id="21a2fb40-2029-11ec-a94b-dd6dc2fa4f6e" data-pub-type="image-with-caption" role="group">
                <div>
                 <pub-hide-empty-link>
                  <a class="b1cw4fo1 pub__link pub__link--black" href="https://www.ikea.com/ma/fr/cat/pax-systeme-19086/">
                   <div class="g5qtjc5 gxo7hqh h1f0e657 r5llg8g" style="height:auto;padding-bottom:56.2%;padding-left:0">
                    <div class="i1llvon7">
                     <img alt="Système PAX." loading="lazy" onerror="this.onerror=null; const parent = this.closest('div'); parent.classList.add('e6qunvq')" sizes="(min-width: 56.25em) 25vw, (min-width: 37.5em) 40vw, 90vw" src="https://www.ikea.com/images/systeme-pax-ecea5d9ca41c75199cc424e13c60e0f7.jpg?f=s" srcset="https://www.ikea.com/images/systeme-pax-ecea5d9ca41c75199cc424e13c60e0f7.jpg?f=sg 1600w,
  https://www.ikea.com/images/systeme-pax-ecea5d9ca41c75199cc424e13c60e0f7.jpg?f=xxxl 1400w,
  https://www.ikea.com/images/systeme-pax-ecea5d9ca41c75199cc424e13c60e0f7.jpg?f=xxl 950w,
  https://www.ikea.com/images/systeme-pax-ecea5d9ca41c75199cc424e13c60e0f7.jpg?f=xl 800w,
  https://www.ikea.com/images/systeme-pax-ecea5d9ca41c75199cc424e13c60e0f7.jpg?f=l 750w,
  https://www.ikea.com/images/systeme-pax-ecea5d9ca41c75199cc424e13c60e0f7.jpg?f=m 600w,
  https://www.ikea.com/images/systeme-pax-ecea5d9ca41c75199cc424e13c60e0f7.jpg?f=s 500w,
  https://www.ikea.com/images/systeme-pax-ecea5d9ca41c75199cc424e13c60e0f7.jpg?f=xs 400w,
  https://www.ikea.com/images/systeme-pax-ecea5d9ca41c75199cc424e13c60e0f7.jpg?f=xxs 300w,
  https://www.ikea.com/images/systeme-pax-ecea5d9ca41c75199cc424e13c60e0f7.jpg?f=xxxs 240w"/>
                    </div>
                   </div>
                  </a>
                 </pub-hide-empty-link>
                </div>
                <figcaption class="i1ycpxq9 pub__designSystemText t91kxqv">
                 Système PAX – solution de rangement personnalisée avec les aménagements de votre choix
                </figcaption>
               </figure>
              </div>
             </div>
            </div>
            <div class="s1cmcu6f">
             <div class="gd8xc1c vz2frqh v18by0fb">
              <div id="228dd070-2029-11ec-a94b-dd6dc2fa4f6e">
               <figure class="gd8xc1c v1tibsle gqfus6o v18by0fb" data-pub-id="228dd070-2029-11ec-a94b-dd6dc2fa4f6e" data-pub-type="image-with-caption" role="group">
                <div>
                 <pub-hide-empty-link>
                  <a class="b1cw4fo1 pub__link pub__link--black" href="https://www.ikea.com/ma/fr/cat/jonaxel-systeme-45730/">
                   <div class="g5qtjc5 gxo7hqh h1f0e657 r5llg8g" style="height:auto;padding-bottom:56.2%;padding-left:0">
                    <div class="i1llvon7">
                     <img alt="Système JONAXEL." loading="lazy" onerror="this.onerror=null; const parent = this.closest('div'); parent.classList.add('e6qunvq')" sizes="(min-width: 56.25em) 25vw, (min-width: 37.5em) 40vw, 90vw" src="https://www.ikea.com/images/systeme-jonaxel-5f3a59c3e291bf63cde7e1c7eb00f51f.jpg?f=s" srcset="https://www.ikea.com/images/systeme-jonaxel-5f3a59c3e291bf63cde7e1c7eb00f51f.jpg?f=sg 1600w,
  https://www.ikea.com/images/systeme-jonaxel-5f3a59c3e291bf63cde7e1c7eb00f51f.jpg?f=xxxl 1400w,
  https://www.ikea.com/images/systeme-jonaxel-5f3a59c3e291bf63cde7e1c7eb00f51f.jpg?f=xxl 950w,
  https://www.ikea.com/images/systeme-jonaxel-5f3a59c3e291bf63cde7e1c7eb00f51f.jpg?f=xl 800w,
  https://www.ikea.com/images/systeme-jonaxel-5f3a59c3e291bf63cde7e1c7eb00f51f.jpg?f=l 750w,
  https://www.ikea.com/images/systeme-jonaxel-5f3a59c3e291bf63cde7e1c7eb00f51f.jpg?f=m 600w,
  https://www.ikea.com/images/systeme-jonaxel-5f3a59c3e291bf63cde7e1c7eb00f51f.jpg?f=s 500w,
  https://www.ikea.com/images/systeme-jonaxel-5f3a59c3e291bf63cde7e1c7eb00f51f.jpg?f=xs 400w,
  https://www.ikea.com/images/systeme-jonaxel-5f3a59c3e291bf63cde7e1c7eb00f51f.jpg?f=xxs 300w,
  https://www.ikea.com/images/systeme-jonaxel-5f3a59c3e291bf63cde7e1c7eb00f51f.jpg?f=xxxs 240w"/>
                    </div>
                   </div>
                  </a>
                 </pub-hide-empty-link>
                </div>
                <figcaption class="i1ycpxq9 pub__designSystemText t91kxqv">
                 Système JONAXEL – rangements ouverts pour un accès aisé, à des prix attrayants
                </figcaption>
               </figure>
              </div>
             </div>
            </div>
           </div>
          </div>
         </div>
        </section>
        <section class="gd8xc1c v19w64p3 v18by0fb">
         <div id="4c661830-2029-11ec-a94b-dd6dc2fa4f6e">
          <div data-pub-id="4c661830-2029-11ec-a94b-dd6dc2fa4f6e" data-pub-type="container">
           <div class="cmmh5q7 xbcjakg mj54kgs l1twdhvz x1aacaiq m1l3ov8s mfmjk3b mqpv3tm mw61hmb mc0hq6s s1vteuqm">
            <div class="s1cmcu6f">
             <div class="gd8xc1c vz2frqh v18by0fb">
              <div id="4f408860-2029-11ec-a94b-dd6dc2fa4f6e">
               <figure class="gd8xc1c v1tibsle gqfus6o v18by0fb" data-pub-id="4f408860-2029-11ec-a94b-dd6dc2fa4f6e" data-pub-type="image-with-caption" role="group">
                <div>
                 <pub-hide-empty-link>
                  <a class="b1cw4fo1 pub__link pub__link--black" href="https://www.ikea.com/ma/fr/cat/elvarli-systeme-35766/">
                   <div class="g5qtjc5 gxo7hqh h1f0e657 r5llg8g" style="height:auto;padding-bottom:56.2%;padding-left:0">
                    <div class="i1llvon7">
                     <img alt="Système ELVARLI." loading="lazy" onerror="this.onerror=null; const parent = this.closest('div'); parent.classList.add('e6qunvq')" sizes="(min-width: 56.25em) 25vw, (min-width: 37.5em) 40vw, 90vw" src="https://www.ikea.com/images/systeme-elvarli-2a16dbef91c5407943a11351cee18331.jpg?f=s" srcset="https://www.ikea.com/images/systeme-elvarli-2a16dbef91c5407943a11351cee18331.jpg?f=sg 1600w,
  https://www.ikea.com/images/systeme-elvarli-2a16dbef91c5407943a11351cee18331.jpg?f=xxxl 1400w,
  https://www.ikea.com/images/systeme-elvarli-2a16dbef91c5407943a11351cee18331.jpg?f=xxl 950w,
  https://www.ikea.com/images/systeme-elvarli-2a16dbef91c5407943a11351cee18331.jpg?f=xl 800w,
  https://www.ikea.com/images/systeme-elvarli-2a16dbef91c5407943a11351cee18331.jpg?f=l 750w,
  https://www.ikea.com/images/systeme-elvarli-2a16dbef91c5407943a11351cee18331.jpg?f=m 600w,
  https://www.ikea.com/images/systeme-elvarli-2a16dbef91c5407943a11351cee18331.jpg?f=s 500w,
  https://www.ikea.com/images/systeme-elvarli-2a16dbef91c5407943a11351cee18331.jpg?f=xs 400w,
  https://www.ikea.com/images/systeme-elvarli-2a16dbef91c5407943a11351cee18331.jpg?f=xxs 300w,
  https://www.ikea.com/images/systeme-elvarli-2a16dbef91c5407943a11351cee18331.jpg?f=xxxs 240w"/>
                    </div>
                   </div>
                  </a>
                 </pub-hide-empty-link>
                </div>
                <figcaption class="i1ycpxq9 pub__designSystemText t91kxqv">
                 Système ELVARLI – système modulaire permettant de concevoir une armoire ouverte parfaitement adaptée à l’espace
                </figcaption>
               </figure>
              </div>
             </div>
            </div>
            <div class="s1cmcu6f">
             <div class="gd8xc1c vz2frqh v18by0fb">
              <div id="503a2aa0-2029-11ec-a94b-dd6dc2fa4f6e">
               <figure class="gd8xc1c v1tibsle gqfus6o v18by0fb" data-pub-id="503a2aa0-2029-11ec-a94b-dd6dc2fa4f6e" data-pub-type="image-with-caption" role="group">
                <div>
                 <pub-hide-empty-link>
                  <a class="b1cw4fo1 pub__link pub__link--black" href="https://www.ikea.com/ma/fr/cat/smastad-systeme-49140/">
                   <div class="g5qtjc5 gxo7hqh h1f0e657 r5llg8g" style="height:auto;padding-bottom:56.2%;padding-left:0">
                    <div class="i1llvon7">
                     <img alt="Système SMÅSTAD." loading="lazy" onerror="this.onerror=null; const parent = this.closest('div'); parent.classList.add('e6qunvq')" sizes="(min-width: 56.25em) 25vw, (min-width: 37.5em) 40vw, 90vw" src="https://www.ikea.com/images/systeme-smastad-6131e721c313b716676ebf0cffce22a6.jpg?f=s" srcset="https://www.ikea.com/images/systeme-smastad-6131e721c313b716676ebf0cffce22a6.jpg?f=sg 1600w,
  https://www.ikea.com/images/systeme-smastad-6131e721c313b716676ebf0cffce22a6.jpg?f=xxxl 1400w,
  https://www.ikea.com/images/systeme-smastad-6131e721c313b716676ebf0cffce22a6.jpg?f=xxl 950w,
  https://www.ikea.com/images/systeme-smastad-6131e721c313b716676ebf0cffce22a6.jpg?f=xl 800w,
  https://www.ikea.com/images/systeme-smastad-6131e721c313b716676ebf0cffce22a6.jpg?f=l 750w,
  https://www.ikea.com/images/systeme-smastad-6131e721c313b716676ebf0cffce22a6.jpg?f=m 600w,
  https://www.ikea.com/images/systeme-smastad-6131e721c313b716676ebf0cffce22a6.jpg?f=s 500w,
  https://www.ikea.com/images/systeme-smastad-6131e721c313b716676ebf0cffce22a6.jpg?f=xs 400w,
  https://www.ikea.com/images/systeme-smastad-6131e721c313b716676ebf0cffce22a6.jpg?f=xxs 300w,
  https://www.ikea.com/images/systeme-smastad-6131e721c313b716676ebf0cffce22a6.jpg?f=xxxs 240w"/>
                    </div>
                   </div>
                  </a>
                 </pub-hide-empty-link>
                </div>
                <figcaption class="i1ycpxq9 pub__designSystemText t91kxqv">
                 Système SMÅSTAD – armoires-penderies, rangements et armoires pour enfant, à combiner et à personnaliser
                </figcaption>
               </figure>
              </div>
             </div>
            </div>
            <div class="s1cmcu6f">
             <div class="gd8xc1c vz2frqh v18by0fb">
              <div id="516d5370-2029-11ec-a94b-dd6dc2fa4f6e">
               <figure class="gd8xc1c v1tibsle gqfus6o v18by0fb" data-pub-id="516d5370-2029-11ec-a94b-dd6dc2fa4f6e" data-pub-type="image-with-caption" role="group">
                <div>
                 <pub-hide-empty-link>
                  <a class="b1cw4fo1 pub__link pub__link--black" href="https://www.ikea.com/ma/fr/cat/boaxel-systeme-47394/">
                   <div class="g5qtjc5 gxo7hqh h1f0e657 r5llg8g" style="height:auto;padding-bottom:56.2%;padding-left:0">
                    <div class="i1llvon7">
                     <img alt="Système BOAXEL." loading="lazy" onerror="this.onerror=null; const parent = this.closest('div'); parent.classList.add('e6qunvq')" sizes="(min-width: 56.25em) 25vw, (min-width: 37.5em) 40vw, 90vw" src="https://www.ikea.com/images/systeme-boaxel-d470e2c4421434a08920a77cad2a763f.jpg?f=s" srcset="https://www.ikea.com/images/systeme-boaxel-d470e2c4421434a08920a77cad2a763f.jpg?f=sg 1600w,
  https://www.ikea.com/images/systeme-boaxel-d470e2c4421434a08920a77cad2a763f.jpg?f=xxxl 1400w,
  https://www.ikea.com/images/systeme-boaxel-d470e2c4421434a08920a77cad2a763f.jpg?f=xxl 950w,
  https://www.ikea.com/images/systeme-boaxel-d470e2c4421434a08920a77cad2a763f.jpg?f=xl 800w,
  https://www.ikea.com/images/systeme-boaxel-d470e2c4421434a08920a77cad2a763f.jpg?f=l 750w,
  https://www.ikea.com/images/systeme-boaxel-d470e2c4421434a08920a77cad2a763f.jpg?f=m 600w,
  https://www.ikea.com/images/systeme-boaxel-d470e2c4421434a08920a77cad2a763f.jpg?f=s 500w,
  https://www.ikea.com/images/systeme-boaxel-d470e2c4421434a08920a77cad2a763f.jpg?f=xs 400w,
  https://www.ikea.com/images/systeme-boaxel-d470e2c4421434a08920a77cad2a763f.jpg?f=xxs 300w,
  https://www.ikea.com/images/systeme-boaxel-d470e2c4421434a08920a77cad2a763f.jpg?f=xxxs 240w"/>
                    </div>
                   </div>
                  </a>
                 </pub-hide-empty-link>
                </div>
                <figcaption class="i1ycpxq9 pub__designSystemText t91kxqv">
                 Système BOAXEL – combinaisons d’armoires-penderies et étagères polyvalentes et abordables pour les vêtements, la lessive et les hobbies
                </figcaption>
               </figure>
              </div>
             </div>
            </div>
           </div>
          </div>
         </div>
        </section>
        <section class="gd8xc1c v19w64p3 v18by0fb">
         <div id="7e314970-2029-11ec-a94b-dd6dc2fa4f6e">
          <div class="o40z9vt">
           <div class="pub__teaser t8ilr1w" data-pub-id="7e314970-2029-11ec-a94b-dd6dc2fa4f6e" data-pub-type="curated-gallery">
            <div class="pub__teaser__grid">
             <div class="pub__teaser__info-container">
              <div class="pub__teaser__info">
               <h2 class="pub__h2 s1gshh7t x1eq9mu0">
                Pour tout ce qui fait battre votre cœur plus vite
               </h2>
               <p class="pub__teaser__description">
                Vous collectionnez les verres colorés? Vous avez des horloges de toutes les formes et tailles? Des céramiques, des jouets, des souvenirs, des œuvres d’art? Quelle que votre ta passion, accordez-lui une place d’honneur dans une jolie vitrine.
               </p>
              </div>
              <a class="pub__btn pub__btn--small pub__btn--secondary pub__teaser__top-button" href="https://www.ikea.com/ma/fr/cat/vitrines-10410/" role="button">
               <span class="pub__btn__inner">
                <span class="pub__btn__label">
                 Voir toutes nos vitrines
                </span>
               </span>
              </a>
             </div>
             <div class="pub__teaser__content">
              <div class="ch1zux0 irbr3cr">
               <div class="ctfct6o">
                <div class="cwrkyzi">
                 <div data-pub-hydrate="pub-shoppable-image" data-seed='{"categoryUrl":"https://www.ikea.com/ma/fr/ideas/fabrikoer-glittrig-dekad-gaenga-recwxso94yb","isLarge":true,"products":[{"dotCoordinates":{"x":62.8,"y":58.2},"productId":"art,80460125","name":"FABRIKÖR"}],"aspectRatioImageProps":{"src":"https://www.ikea.com/ext/ingkadam/m/59d9d9b902d839df/original/PH183052-crop001.jpg?f=s","srcSet":"https://www.ikea.com/ext/ingkadam/m/59d9d9b902d839df/original/PH183052-crop001.jpg?f=sg 1600w,\n  https://www.ikea.com/ext/ingkadam/m/59d9d9b902d839df/original/PH183052-crop001.jpg?f=xxxl 1400w,\n  https://www.ikea.com/ext/ingkadam/m/59d9d9b902d839df/original/PH183052-crop001.jpg?f=xxl 950w,\n  https://www.ikea.com/ext/ingkadam/m/59d9d9b902d839df/original/PH183052-crop001.jpg?f=xl 800w,\n  https://www.ikea.com/ext/ingkadam/m/59d9d9b902d839df/original/PH183052-crop001.jpg?f=l 750w,\n  https://www.ikea.com/ext/ingkadam/m/59d9d9b902d839df/original/PH183052-crop001.jpg?f=m 600w,\n  https://www.ikea.com/ext/ingkadam/m/59d9d9b902d839df/original/PH183052-crop001.jpg?f=s 500w,\n  https://www.ikea.com/ext/ingkadam/m/59d9d9b902d839df/original/PH183052-crop001.jpg?f=xs 400w,\n  https://www.ikea.com/ext/ingkadam/m/59d9d9b902d839df/original/PH183052-crop001.jpg?f=xxs 300w,\n  https://www.ikea.com/ext/ingkadam/m/59d9d9b902d839df/original/PH183052-crop001.jpg?f=xxxs 240w","sizes":"(min-width: 112.5em) 789px, (min-width: 56.25em) 43vw, 88vw","prefix":"pub__","alt":"Vitrine FABRIKÖR jaune clair où est exposée une collection d’horloges, contre un mur mauve orné lui-même de deux horloges.","ratio":"portrait"},"productFragmentsEsiUrl":"https://www.ikea.com/ma/fr","disableLink":false,"parentType":"curated-gallery","assetId":"E1FBB1AB-B6CA-481E-8009E050DAAA504E","imageIndex":0}' style="height:100%">
                  <div class="" data-asset-id="E1FBB1AB-B6CA-481E-8009E050DAAA504E" data-parent-type="curated-gallery" data-products="80460125" data-pub-shoppable-image-wrapper="true" style="height:100%">
                   <div class="pub__shoppable-image pub__shoppable-image--visible-dots">
                    <a class="pub__shoppable-image__category-link" href="https://www.ikea.com/ma/fr/ideas/fabrikoer-glittrig-dekad-gaenga-recwxso94yb">
                     <span class="pub__aspect-ratio-image pub__aspect-ratio-image--portrait">
                      <img alt="Vitrine FABRIKÖR jaune clair où est exposée une collection d’horloges, contre un mur mauve orné lui-même de deux horloges." class="pub__aspect-ratio-image__image" loading="lazy" sizes="(min-width: 112.5em) 789px, (min-width: 56.25em) 43vw, 88vw" src="https://www.ikea.com/ext/ingkadam/m/59d9d9b902d839df/original/PH183052-crop001.jpg?f=s" srcset="https://www.ikea.com/ext/ingkadam/m/59d9d9b902d839df/original/PH183052-crop001.jpg?f=sg 1600w,
  https://www.ikea.com/ext/ingkadam/m/59d9d9b902d839df/original/PH183052-crop001.jpg?f=xxxl 1400w,
  https://www.ikea.com/ext/ingkadam/m/59d9d9b902d839df/original/PH183052-crop001.jpg?f=xxl 950w,
  https://www.ikea.com/ext/ingkadam/m/59d9d9b902d839df/original/PH183052-crop001.jpg?f=xl 800w,
  https://www.ikea.com/ext/ingkadam/m/59d9d9b902d839df/original/PH183052-crop001.jpg?f=l 750w,
  https://www.ikea.com/ext/ingkadam/m/59d9d9b902d839df/original/PH183052-crop001.jpg?f=m 600w,
  https://www.ikea.com/ext/ingkadam/m/59d9d9b902d839df/original/PH183052-crop001.jpg?f=s 500w,
  https://www.ikea.com/ext/ingkadam/m/59d9d9b902d839df/original/PH183052-crop001.jpg?f=xs 400w,
  https://www.ikea.com/ext/ingkadam/m/59d9d9b902d839df/original/PH183052-crop001.jpg?f=xxs 300w,
  https://www.ikea.com/ext/ingkadam/m/59d9d9b902d839df/original/PH183052-crop001.jpg?f=xxxs 240w"/>
                     </span>
                    </a>
                    <div class="pub__aspect-ratio-box pub__aspect-ratio-box--portrait pub__shoppable-image__aspect-constraint">
                     <div aria-hidden="false" class="pub__shoppable-image__area pub__shoppable-image__area--active" style="top:-100%;left:-100%">
                      <a aria-labelledby="pub__shoppable-image-art,80460125" class="pub__shoppable-image__dot" href="">
                      </a>
                      <div aria-hidden="false" class="pub__shoppable-image__tag pub__shoppable-image__tag--left" id="pub__shoppable-image-art,80460125" role="tooltip">
                       <div class="pub__shoppable-image__tag-inner">
                        <div>
                        </div>
                        <span class="pub__shoppable-image__sr-description">
                         go to product page
                        </span>
                       </div>
                      </div>
                     </div>
                    </div>
                   </div>
                  </div>
                 </div>
                </div>
                <div class="cwrkyzi">
                 <div data-pub-hydrate="pub-shoppable-image" data-seed='{"categoryUrl":"https://www.ikea.com/ma/fr/ideas/enhet-beraekna-gradvis-tonsaetta-rec0447i8ms","isLarge":true,"products":[{"dotCoordinates":{"x":56.4,"y":51.3},"productId":"art,60448945","name":"ENHET"}],"aspectRatioImageProps":{"src":"https://www.ikea.com/ext/ingkadam/m/5ae220610e2daa9a/original/PH183051.jpg?f=s","srcSet":"https://www.ikea.com/ext/ingkadam/m/5ae220610e2daa9a/original/PH183051.jpg?f=sg 1600w,\n  https://www.ikea.com/ext/ingkadam/m/5ae220610e2daa9a/original/PH183051.jpg?f=xxxl 1400w,\n  https://www.ikea.com/ext/ingkadam/m/5ae220610e2daa9a/original/PH183051.jpg?f=xxl 950w,\n  https://www.ikea.com/ext/ingkadam/m/5ae220610e2daa9a/original/PH183051.jpg?f=xl 800w,\n  https://www.ikea.com/ext/ingkadam/m/5ae220610e2daa9a/original/PH183051.jpg?f=l 750w,\n  https://www.ikea.com/ext/ingkadam/m/5ae220610e2daa9a/original/PH183051.jpg?f=m 600w,\n  https://www.ikea.com/ext/ingkadam/m/5ae220610e2daa9a/original/PH183051.jpg?f=s 500w,\n  https://www.ikea.com/ext/ingkadam/m/5ae220610e2daa9a/original/PH183051.jpg?f=xs 400w,\n  https://www.ikea.com/ext/ingkadam/m/5ae220610e2daa9a/original/PH183051.jpg?f=xxs 300w,\n  https://www.ikea.com/ext/ingkadam/m/5ae220610e2daa9a/original/PH183051.jpg?f=xxxs 240w","sizes":"(min-width: 112.5em) 789px, (min-width: 56.25em) 43vw, 88vw","prefix":"pub__","alt":"Éléments ENHET noirs où sont exposés des verres et des vases colorés, contre un mur mauve.","ratio":"portrait"},"productFragmentsEsiUrl":"https://www.ikea.com/ma/fr","disableLink":false,"parentType":"curated-gallery","assetId":"B0280385-5B6F-4A86-BB4EB4826A9DE9DD","imageIndex":1}' style="height:100%">
                  <div class="" data-asset-id="B0280385-5B6F-4A86-BB4EB4826A9DE9DD" data-parent-type="curated-gallery" data-products="60448945" data-pub-shoppable-image-wrapper="true" style="height:100%">
                   <div class="pub__shoppable-image pub__shoppable-image--visible-dots">
                    <a class="pub__shoppable-image__category-link" href="https://www.ikea.com/ma/fr/ideas/enhet-beraekna-gradvis-tonsaetta-rec0447i8ms">
                     <span class="pub__aspect-ratio-image pub__aspect-ratio-image--portrait">
                      <img alt="Éléments ENHET noirs où sont exposés des verres et des vases colorés, contre un mur mauve." class="pub__aspect-ratio-image__image" loading="lazy" sizes="(min-width: 112.5em) 789px, (min-width: 56.25em) 43vw, 88vw" src="https://www.ikea.com/ext/ingkadam/m/5ae220610e2daa9a/original/PH183051.jpg?f=s" srcset="https://www.ikea.com/ext/ingkadam/m/5ae220610e2daa9a/original/PH183051.jpg?f=sg 1600w,
  https://www.ikea.com/ext/ingkadam/m/5ae220610e2daa9a/original/PH183051.jpg?f=xxxl 1400w,
  https://www.ikea.com/ext/ingkadam/m/5ae220610e2daa9a/original/PH183051.jpg?f=xxl 950w,
  https://www.ikea.com/ext/ingkadam/m/5ae220610e2daa9a/original/PH183051.jpg?f=xl 800w,
  https://www.ikea.com/ext/ingkadam/m/5ae220610e2daa9a/original/PH183051.jpg?f=l 750w,
  https://www.ikea.com/ext/ingkadam/m/5ae220610e2daa9a/original/PH183051.jpg?f=m 600w,
  https://www.ikea.com/ext/ingkadam/m/5ae220610e2daa9a/original/PH183051.jpg?f=s 500w,
  https://www.ikea.com/ext/ingkadam/m/5ae220610e2daa9a/original/PH183051.jpg?f=xs 400w,
  https://www.ikea.com/ext/ingkadam/m/5ae220610e2daa9a/original/PH183051.jpg?f=xxs 300w,
  https://www.ikea.com/ext/ingkadam/m/5ae220610e2daa9a/original/PH183051.jpg?f=xxxs 240w"/>
                     </span>
                    </a>
                    <div class="pub__aspect-ratio-box pub__aspect-ratio-box--portrait pub__shoppable-image__aspect-constraint">
                     <div aria-hidden="false" class="pub__shoppable-image__area pub__shoppable-image__area--active" style="top:-100%;left:-100%">
                      <a aria-labelledby="pub__shoppable-image-art,60448945" class="pub__shoppable-image__dot" href="">
                      </a>
                      <div aria-hidden="false" class="pub__shoppable-image__tag pub__shoppable-image__tag--bottom" id="pub__shoppable-image-art,60448945" role="tooltip">
                       <div class="pub__shoppable-image__tag-inner">
                        <div>
                        </div>
                        <span class="pub__shoppable-image__sr-description">
                         go to product page
                        </span>
                       </div>
                      </div>
                     </div>
                    </div>
                   </div>
                  </div>
                 </div>
                </div>
               </div>
              </div>
             </div>
             <a class="pub__teaser__bottom-button pub__chunky-header pub__chunky-header--small" href="https://www.ikea.com/ma/fr/cat/vitrines-10410/">
              <span class="pub__chunky-header__title-wrapper">
               <span class="pub__chunky-header__title">
                Voir toutes nos vitrines
               </span>
              </span>
              <svg aria-hidden="true" class="pub__svg-icon pub__chunky-header__icon" focusable="false" viewbox="0 0 24 24">
               <path clip-rule="evenodd" d="m15.5996 12.0007-5.785 5.7857-1.4143-1.4141 4.3711-4.3716L8.4003 7.629l1.4143-1.4142 5.785 5.7859z" fill-rule="evenodd">
               </path>
              </svg>
             </a>
            </div>
           </div>
          </div>
         </div>
        </section>
        <section class="gd8xc1c v19w64p3 v18by0fb">
         <div id="daff86d0-2029-11ec-96f0-d900bf02a083">
          <div class="o40z9vt">
           <div class="pub__teaser t8ilr1w" data-pub-id="daff86d0-2029-11ec-96f0-d900bf02a083" data-pub-type="inspiration-card">
            <div class="pub__teaser__grid">
             <div class="pub__teaser__info-container">
              <div class="pub__teaser__info">
               <h2 class="pub__h2 s1gshh7t x1eq9mu0">
                Idées astucieuses pour logement polyvalent
               </h2>
              </div>
             </div>
             <div class="pub__teaser__content">
              <div data-pub-hydrate="pub-carousel" data-seed='{"id":"daff86d0-2029-11ec-96f0-d900bf02a083","prefix":"pub__","contentClass":"c4pwwkx","itemClass":"i12pyk82","bodyWrapperClass":"bpftgzm","rtl":false,"role":"list","skipButtonText":"Sauter la liste","ariaLabelLeftBtn":"Diapo précédente","ariaLabelRightBtn":"Diapo suivante"}' style="height:100%">
               <div class="pub__carousel" role="list" tabindex="-1">
                <a class="btn btn--primary-inverse pub__carousel__skip-button" href="#pub__-carousel__daff86d0-2029-11ec-96f0-d900bf02a083-skip-btn" role="button">
                 <span class="btn__inner">
                  Sauter la liste
                 </span>
                </a>
                <div class="pub__carousel__wrapper">
                 <button aria-controls="pub__carousel__daff86d0-2029-11ec-96f0-d900bf02a083" aria-label="Diapo précédente" class="pub__btn pub__btn--small pub__btn--icon-primary pub__carousel__button" id="pub__-carousel__daff86d0-2029-11ec-96f0-d900bf02a083-prev-btn" type="button">
                  <span class="pub__btn__inner">
                   <svg aria-hidden="true" class="pub__svg-icon pub__btn__icon" focusable="false" viewbox="0 0 24 24">
                    <path clip-rule="evenodd" d="m7 12.0009 8.0012-8.0007 1.4142 1.4142-6.587 6.5866 6.5859 6.5868L15 20.002l-8-8.0011z" fill-rule="evenodd">
                    </path>
                   </svg>
                  </span>
                 </button>
                 <div class="pub__carousel__content c4pwwkx pub__carousel__content--snap-slide">
                  <div class="pub__carousel__body-wrapper bpftgzm">
                   <div class="pub__carousel__body" id="pub__carousel__daff86d0-2029-11ec-96f0-d900bf02a083">
                    <div class="pub__carousel-slide i12pyk82">
                     <div class="f7zhins" data-pub-hydrate-child="pub-carousel" style="height:100%;width:100%">
                      <a class="b1cw4fo1 ddaom9 pub__link pub__link--white" data-pub-id="db0700e0-2029-11ec-96f0-d900bf02a083" data-pub-itemindex="0" data-pub-type="inspiration-card-item" href="https://www.ikea.com/ma/fr/rooms/bedroom/gallery/2-en-1-chambre-damis-douillette-et-atelier-creatif-pub77b5a948" style="height:100%;width:100%">
                       <div class="c30mk8n cinp0wf f7zhins s8monoq" style="height:100%;width:100%">
                        <div class="c1b7q3xo c8u3m6h">
                         <span class="pub__aspect-ratio-image pub__aspect-ratio-image--square f18ghfnk">
                          <img alt="Chambre à coucher douillette sous plafond en pente, lit banquette blanc à trois tiroirs et armoire à 2 portes HAUGA blanche." aria-labelledby="db0700e0-2029-11ec-96f0-d900bf02a083-heading db0700e0-2029-11ec-96f0-d900bf02a083-body" class="pub__aspect-ratio-image__image" loading="lazy" sizes="(min-width: 56.25em) 27vw, (min-width: 37.5em) 43vw, 85vw" src="https://www.ikea.com/images/chambre-a-coucher-douillette-sous-plafond-en-pente-lit-banqu-4f6195560410b6381afe460d1c1a9645.jpg?f=s" srcset="https://www.ikea.com/images/chambre-a-coucher-douillette-sous-plafond-en-pente-lit-banqu-4f6195560410b6381afe460d1c1a9645.jpg?f=sg 1600w,
  https://www.ikea.com/images/chambre-a-coucher-douillette-sous-plafond-en-pente-lit-banqu-4f6195560410b6381afe460d1c1a9645.jpg?f=xxxl 1400w,
  https://www.ikea.com/images/chambre-a-coucher-douillette-sous-plafond-en-pente-lit-banqu-4f6195560410b6381afe460d1c1a9645.jpg?f=xxl 950w,
  https://www.ikea.com/images/chambre-a-coucher-douillette-sous-plafond-en-pente-lit-banqu-4f6195560410b6381afe460d1c1a9645.jpg?f=xl 800w,
  https://www.ikea.com/images/chambre-a-coucher-douillette-sous-plafond-en-pente-lit-banqu-4f6195560410b6381afe460d1c1a9645.jpg?f=l 750w,
  https://www.ikea.com/images/chambre-a-coucher-douillette-sous-plafond-en-pente-lit-banqu-4f6195560410b6381afe460d1c1a9645.jpg?f=m 600w,
  https://www.ikea.com/images/chambre-a-coucher-douillette-sous-plafond-en-pente-lit-banqu-4f6195560410b6381afe460d1c1a9645.jpg?f=s 500w,
  https://www.ikea.com/images/chambre-a-coucher-douillette-sous-plafond-en-pente-lit-banqu-4f6195560410b6381afe460d1c1a9645.jpg?f=xs 400w,
  https://www.ikea.com/images/chambre-a-coucher-douillette-sous-plafond-en-pente-lit-banqu-4f6195560410b6381afe460d1c1a9645.jpg?f=xxs 300w,
  https://www.ikea.com/images/chambre-a-coucher-douillette-sous-plafond-en-pente-lit-banqu-4f6195560410b6381afe460d1c1a9645.jpg?f=xxxs 240w"/>
                         </span>
                        </div>
                        <div class="c1b7q3xo c8u3m6h f7zhins g1mfmhmf g5qtjc5">
                         <div class="b15fs3xm b1asp286 c30mk8n f7zhins g5qtjc5 l1rjie0o lr6adlh" style="width:100%;background-color:#6b3d99">
                          <div class="bgrf0js f1dbvbh0 gd8xc1c v11tpn0s v1duoae3 gqfus6o v18by0fb">
                           <div class="">
                            <div class="gd8xc1c vmq1cv0 v18by0fb">
                             <h3 class="pub__h3 s1gshh7t w19ofv4i">
                              <div class="s1fbln9t" id="db0700e0-2029-11ec-96f0-d900bf02a083-heading">
                               2-en-1: chambre d’amis douillette et atelier créatif
                              </div>
                             </h3>
                            </div>
                           </div>
                           <button aria-hidden="true" class="pub__btn pub__btn--icon-primary-inverse b8b8hey" tabindex="-1" type="button">
                            <span class="pub__btn__inner">
                             <svg aria-hidden="true" class="pub__svg-icon pub__btn__icon" focusable="false" viewbox="0 0 24 24">
                              <path clip-rule="evenodd" d="M19.2937 12.7074L20.0008 12.0003L19.2938 11.2932L12.0008 3.99927L10.5865 5.41339L16.1727 11.0003H4V13.0003H16.1723L10.5855 18.5868L11.9996 20.0011L19.2937 12.7074Z" fill-rule="evenodd">
                              </path>
                             </svg>
                            </span>
                           </button>
                          </div>
                         </div>
                        </div>
                       </div>
                      </a>
                     </div>
                    </div>
                    <div class="pub__carousel-slide i12pyk82">
                     <div class="f7zhins" data-pub-hydrate-child="pub-carousel" style="height:100%;width:100%">
                      <a class="b1cw4fo1 ddaom9 pub__link pub__link--black" data-pub-id="eb4469c0-2029-11ec-96f0-d900bf02a083" data-pub-itemindex="1" data-pub-type="inspiration-card-item" href="https://www.ikea.com/ma/fr/rooms/living-room/gallery/salon-et-chambre-confortables-deux-en-un-pub8fcd6016" style="height:100%;width:100%">
                       <div class="c30mk8n cinp0wf f7zhins s8monoq" style="height:100%;width:100%">
                        <div class="c1b7q3xo c8u3m6h">
                         <span class="pub__aspect-ratio-image pub__aspect-ratio-image--square f18ghfnk">
                          <img alt="Convertible beige clair déployé avec du linge de lit gris. Il se trouve devant une vitrine grise, avec un tapis en jute au sol." aria-labelledby="eb4469c0-2029-11ec-96f0-d900bf02a083-heading eb4469c0-2029-11ec-96f0-d900bf02a083-body" class="pub__aspect-ratio-image__image" loading="lazy" sizes="(min-width: 56.25em) 27vw, (min-width: 37.5em) 43vw, 85vw" src="https://www.ikea.com/images/convertible-beige-clair-deploye-avec-du-linge-de-lit-gris-il-2c9c6f7c0572a4d20ab6133b9402efc6.jpg?f=s" srcset="https://www.ikea.com/images/convertible-beige-clair-deploye-avec-du-linge-de-lit-gris-il-2c9c6f7c0572a4d20ab6133b9402efc6.jpg?f=sg 1600w,
  https://www.ikea.com/images/convertible-beige-clair-deploye-avec-du-linge-de-lit-gris-il-2c9c6f7c0572a4d20ab6133b9402efc6.jpg?f=xxxl 1400w,
  https://www.ikea.com/images/convertible-beige-clair-deploye-avec-du-linge-de-lit-gris-il-2c9c6f7c0572a4d20ab6133b9402efc6.jpg?f=xxl 950w,
  https://www.ikea.com/images/convertible-beige-clair-deploye-avec-du-linge-de-lit-gris-il-2c9c6f7c0572a4d20ab6133b9402efc6.jpg?f=xl 800w,
  https://www.ikea.com/images/convertible-beige-clair-deploye-avec-du-linge-de-lit-gris-il-2c9c6f7c0572a4d20ab6133b9402efc6.jpg?f=l 750w,
  https://www.ikea.com/images/convertible-beige-clair-deploye-avec-du-linge-de-lit-gris-il-2c9c6f7c0572a4d20ab6133b9402efc6.jpg?f=m 600w,
  https://www.ikea.com/images/convertible-beige-clair-deploye-avec-du-linge-de-lit-gris-il-2c9c6f7c0572a4d20ab6133b9402efc6.jpg?f=s 500w,
  https://www.ikea.com/images/convertible-beige-clair-deploye-avec-du-linge-de-lit-gris-il-2c9c6f7c0572a4d20ab6133b9402efc6.jpg?f=xs 400w,
  https://www.ikea.com/images/convertible-beige-clair-deploye-avec-du-linge-de-lit-gris-il-2c9c6f7c0572a4d20ab6133b9402efc6.jpg?f=xxs 300w,
  https://www.ikea.com/images/convertible-beige-clair-deploye-avec-du-linge-de-lit-gris-il-2c9c6f7c0572a4d20ab6133b9402efc6.jpg?f=xxxs 240w"/>
                         </span>
                        </div>
                        <div class="c1b7q3xo c8u3m6h f7zhins g1mfmhmf g5qtjc5">
                         <div class="b15fs3xm b1asp286 c30mk8n f7zhins g5qtjc5 l1rjie0o lr6adlh" style="width:100%;background-color:#00a1e5">
                          <div class="bgrf0js f1dbvbh0 gd8xc1c v11tpn0s v1duoae3 gqfus6o v18by0fb">
                           <div class="">
                            <div class="gd8xc1c vmq1cv0 v18by0fb">
                             <h3 class="g2q85x8 pub__h3 s1gshh7t">
                              <div class="s1fbln9t" id="eb4469c0-2029-11ec-96f0-d900bf02a083-heading">
                               Combo chambre/salon confortable et fonctionnel
                              </div>
                             </h3>
                            </div>
                           </div>
                           <button aria-hidden="true" class="pub__btn pub__btn--icon-primary b8b8hey" tabindex="-1" type="button">
                            <span class="pub__btn__inner">
                             <svg aria-hidden="true" class="pub__svg-icon pub__btn__icon" focusable="false" viewbox="0 0 24 24">
                              <path clip-rule="evenodd" d="M19.2937 12.7074L20.0008 12.0003L19.2938 11.2932L12.0008 3.99927L10.5865 5.41339L16.1727 11.0003H4V13.0003H16.1723L10.5855 18.5868L11.9996 20.0011L19.2937 12.7074Z" fill-rule="evenodd">
                              </path>
                             </svg>
                            </span>
                           </button>
                          </div>
                         </div>
                        </div>
                       </div>
                      </a>
                     </div>
                    </div>
                    <div class="pub__carousel-slide i12pyk82">
                     <div class="f7zhins" data-pub-hydrate-child="pub-carousel" style="height:100%;width:100%">
                      <a class="b1cw4fo1 ddaom9 pub__link pub__link--black" data-pub-id="f9572a70-2029-11ec-96f0-d900bf02a083" data-pub-itemindex="2" data-pub-type="inspiration-card-item" href="https://www.ikea.com/ma/fr/rooms/bedroom/gallery/lorsque-votre-chambre-a-coucher-est-aussi-votre-salon-pubfa3208a7" style="height:100%;width:100%">
                       <div class="c30mk8n cinp0wf f7zhins s8monoq" style="height:100%;width:100%">
                        <div class="c1b7q3xo c8u3m6h">
                         <span class="pub__aspect-ratio-image pub__aspect-ratio-image--square f18ghfnk">
                          <img alt="Chambre à coucher avec cadre de lit matelassé et tête de lit d’angle, housse de couette et taie d’oreiller blanches, plante en pot." aria-labelledby="f9572a70-2029-11ec-96f0-d900bf02a083-heading f9572a70-2029-11ec-96f0-d900bf02a083-body" class="pub__aspect-ratio-image__image" loading="lazy" sizes="(min-width: 56.25em) 27vw, (min-width: 37.5em) 43vw, 85vw" src="https://www.ikea.com/images/chambre-a-coucher-avec-cadre-de-lit-matelasse-et-tete-de-lit-9435fd9efefbffabe5621372f0325aff.jpg?f=s" srcset="https://www.ikea.com/images/chambre-a-coucher-avec-cadre-de-lit-matelasse-et-tete-de-lit-9435fd9efefbffabe5621372f0325aff.jpg?f=sg 1600w,
  https://www.ikea.com/images/chambre-a-coucher-avec-cadre-de-lit-matelasse-et-tete-de-lit-9435fd9efefbffabe5621372f0325aff.jpg?f=xxxl 1400w,
  https://www.ikea.com/images/chambre-a-coucher-avec-cadre-de-lit-matelasse-et-tete-de-lit-9435fd9efefbffabe5621372f0325aff.jpg?f=xxl 950w,
  https://www.ikea.com/images/chambre-a-coucher-avec-cadre-de-lit-matelasse-et-tete-de-lit-9435fd9efefbffabe5621372f0325aff.jpg?f=xl 800w,
  https://www.ikea.com/images/chambre-a-coucher-avec-cadre-de-lit-matelasse-et-tete-de-lit-9435fd9efefbffabe5621372f0325aff.jpg?f=l 750w,
  https://www.ikea.com/images/chambre-a-coucher-avec-cadre-de-lit-matelasse-et-tete-de-lit-9435fd9efefbffabe5621372f0325aff.jpg?f=m 600w,
  https://www.ikea.com/images/chambre-a-coucher-avec-cadre-de-lit-matelasse-et-tete-de-lit-9435fd9efefbffabe5621372f0325aff.jpg?f=s 500w,
  https://www.ikea.com/images/chambre-a-coucher-avec-cadre-de-lit-matelasse-et-tete-de-lit-9435fd9efefbffabe5621372f0325aff.jpg?f=xs 400w,
  https://www.ikea.com/images/chambre-a-coucher-avec-cadre-de-lit-matelasse-et-tete-de-lit-9435fd9efefbffabe5621372f0325aff.jpg?f=xxs 300w,
  https://www.ikea.com/images/chambre-a-coucher-avec-cadre-de-lit-matelasse-et-tete-de-lit-9435fd9efefbffabe5621372f0325aff.jpg?f=xxxs 240w"/>
                         </span>
                        </div>
                        <div class="c1b7q3xo c8u3m6h f7zhins g1mfmhmf g5qtjc5">
                         <div class="b15fs3xm b1asp286 c30mk8n f7zhins g5qtjc5 l1rjie0o lr6adlh" style="width:100%;background-color:#ffaa00">
                          <div class="bgrf0js f1dbvbh0 gd8xc1c v11tpn0s v1duoae3 gqfus6o v18by0fb">
                           <div class="">
                            <div class="gd8xc1c vmq1cv0 v18by0fb">
                             <h3 class="g2q85x8 pub__h3 s1gshh7t">
                              <div class="s1fbln9t" id="f9572a70-2029-11ec-96f0-d900bf02a083-heading">
                               Lorsque la chambre à coucher est aussi le salon
                              </div>
                             </h3>
                            </div>
                           </div>
                           <button aria-hidden="true" class="pub__btn pub__btn--icon-primary b8b8hey" tabindex="-1" type="button">
                            <span class="pub__btn__inner">
                             <svg aria-hidden="true" class="pub__svg-icon pub__btn__icon" focusable="false" viewbox="0 0 24 24">
                              <path clip-rule="evenodd" d="M19.2937 12.7074L20.0008 12.0003L19.2938 11.2932L12.0008 3.99927L10.5865 5.41339L16.1727 11.0003H4V13.0003H16.1723L10.5855 18.5868L11.9996 20.0011L19.2937 12.7074Z" fill-rule="evenodd">
                              </path>
                             </svg>
                            </span>
                           </button>
                          </div>
                         </div>
                        </div>
                       </div>
                      </a>
                     </div>
                    </div>
                    <div class="pub__carousel-slide i12pyk82">
                     <div class="f7zhins" data-pub-hydrate-child="pub-carousel" style="height:100%;width:100%">
                      <a class="b1cw4fo1 ddaom9 pub__link pub__link--black" data-pub-id="0ac65c90-202a-11ec-96f0-d900bf02a083" data-pub-itemindex="3" data-pub-type="inspiration-card-item" href="https://www.ikea.com/ma/fr/rooms/living-room/gallery/une-piece-de-vie-plaisante-et-dynamique-pub2867d718" style="height:100%;width:100%">
                       <div class="c30mk8n cinp0wf f7zhins s8monoq" style="height:100%;width:100%">
                        <div class="c1b7q3xo c8u3m6h">
                         <span class="pub__aspect-ratio-image pub__aspect-ratio-image--square f18ghfnk">
                          <img alt="Petit studio avec convertible 2 places LYCKSELE revêtu d’une housse Vansbro vert clair, textiles en noir et blanc et fauteuil." aria-labelledby="0ac65c90-202a-11ec-96f0-d900bf02a083-heading 0ac65c90-202a-11ec-96f0-d900bf02a083-body" class="pub__aspect-ratio-image__image" loading="lazy" sizes="(min-width: 56.25em) 27vw, (min-width: 37.5em) 43vw, 85vw" src="https://www.ikea.com/images/petit-studio-avec-convertible-2-places-lycksele-revetu-dune--8c6593a2f746c575ea656452aa1a1fa1.jpg?f=s" srcset="https://www.ikea.com/images/petit-studio-avec-convertible-2-places-lycksele-revetu-dune--8c6593a2f746c575ea656452aa1a1fa1.jpg?f=sg 1600w,
  https://www.ikea.com/images/petit-studio-avec-convertible-2-places-lycksele-revetu-dune--8c6593a2f746c575ea656452aa1a1fa1.jpg?f=xxxl 1400w,
  https://www.ikea.com/images/petit-studio-avec-convertible-2-places-lycksele-revetu-dune--8c6593a2f746c575ea656452aa1a1fa1.jpg?f=xxl 950w,
  https://www.ikea.com/images/petit-studio-avec-convertible-2-places-lycksele-revetu-dune--8c6593a2f746c575ea656452aa1a1fa1.jpg?f=xl 800w,
  https://www.ikea.com/images/petit-studio-avec-convertible-2-places-lycksele-revetu-dune--8c6593a2f746c575ea656452aa1a1fa1.jpg?f=l 750w,
  https://www.ikea.com/images/petit-studio-avec-convertible-2-places-lycksele-revetu-dune--8c6593a2f746c575ea656452aa1a1fa1.jpg?f=m 600w,
  https://www.ikea.com/images/petit-studio-avec-convertible-2-places-lycksele-revetu-dune--8c6593a2f746c575ea656452aa1a1fa1.jpg?f=s 500w,
  https://www.ikea.com/images/petit-studio-avec-convertible-2-places-lycksele-revetu-dune--8c6593a2f746c575ea656452aa1a1fa1.jpg?f=xs 400w,
  https://www.ikea.com/images/petit-studio-avec-convertible-2-places-lycksele-revetu-dune--8c6593a2f746c575ea656452aa1a1fa1.jpg?f=xxs 300w,
  https://www.ikea.com/images/petit-studio-avec-convertible-2-places-lycksele-revetu-dune--8c6593a2f746c575ea656452aa1a1fa1.jpg?f=xxxs 240w"/>
                         </span>
                        </div>
                        <div class="c1b7q3xo c8u3m6h f7zhins g1mfmhmf g5qtjc5">
                         <div class="b15fs3xm b1asp286 c30mk8n f7zhins g5qtjc5 l1rjie0o lr6adlh" style="width:100%;background-color:#78bf30">
                          <div class="bgrf0js f1dbvbh0 gd8xc1c v11tpn0s v1duoae3 gqfus6o v18by0fb">
                           <div class="">
                            <div class="gd8xc1c vmq1cv0 v18by0fb">
                             <h3 class="g2q85x8 pub__h3 s1gshh7t">
                              <div class="s1fbln9t" id="0ac65c90-202a-11ec-96f0-d900bf02a083-heading">
                               Une pièce de vie plaisante et dynamique
                              </div>
                             </h3>
                            </div>
                           </div>
                           <button aria-hidden="true" class="pub__btn pub__btn--icon-primary b8b8hey" tabindex="-1" type="button">
                            <span class="pub__btn__inner">
                             <svg aria-hidden="true" class="pub__svg-icon pub__btn__icon" focusable="false" viewbox="0 0 24 24">
                              <path clip-rule="evenodd" d="M19.2937 12.7074L20.0008 12.0003L19.2938 11.2932L12.0008 3.99927L10.5865 5.41339L16.1727 11.0003H4V13.0003H16.1723L10.5855 18.5868L11.9996 20.0011L19.2937 12.7074Z" fill-rule="evenodd">
                              </path>
                             </svg>
                            </span>
                           </button>
                          </div>
                         </div>
                        </div>
                       </div>
                      </a>
                     </div>
                    </div>
                    <div class="pub__carousel-slide i12pyk82">
                     <div class="f7zhins" data-pub-hydrate-child="pub-carousel" style="height:100%;width:100%">
                      <a class="b1cw4fo1 ddaom9 pub__link pub__link--black" data-pub-id="276330d0-202a-11ec-96f0-d900bf02a083" data-pub-itemindex="4" data-pub-type="inspiration-card-item" href="https://www.ikea.com/ma/fr/rooms/living-room/how-to/un-salon-pour-les-grasses-matinees-pub6b33f6b0" style="height:100%;width:100%">
                       <div class="c30mk8n cinp0wf f7zhins s8monoq" style="height:100%;width:100%">
                        <div class="c1b7q3xo c8u3m6h">
                         <span class="pub__aspect-ratio-image pub__aspect-ratio-image--square f18ghfnk">
                          <img alt="Salon compact, convertible avec méridienne d’un côté, buffet, rangements, TV, stéréo et tableaux de l’autre." aria-labelledby="276330d0-202a-11ec-96f0-d900bf02a083-heading 276330d0-202a-11ec-96f0-d900bf02a083-body" class="pub__aspect-ratio-image__image" loading="lazy" sizes="(min-width: 56.25em) 27vw, (min-width: 37.5em) 43vw, 85vw" src="https://www.ikea.com/images/salon-compact-convertible-avec-meridienne-dun-cote-buffet-ra-f957bac4b2e4524bcafb3b821eda0ab5.jpg?f=s" srcset="https://www.ikea.com/images/salon-compact-convertible-avec-meridienne-dun-cote-buffet-ra-f957bac4b2e4524bcafb3b821eda0ab5.jpg?f=sg 1600w,
  https://www.ikea.com/images/salon-compact-convertible-avec-meridienne-dun-cote-buffet-ra-f957bac4b2e4524bcafb3b821eda0ab5.jpg?f=xxxl 1400w,
  https://www.ikea.com/images/salon-compact-convertible-avec-meridienne-dun-cote-buffet-ra-f957bac4b2e4524bcafb3b821eda0ab5.jpg?f=xxl 950w,
  https://www.ikea.com/images/salon-compact-convertible-avec-meridienne-dun-cote-buffet-ra-f957bac4b2e4524bcafb3b821eda0ab5.jpg?f=xl 800w,
  https://www.ikea.com/images/salon-compact-convertible-avec-meridienne-dun-cote-buffet-ra-f957bac4b2e4524bcafb3b821eda0ab5.jpg?f=l 750w,
  https://www.ikea.com/images/salon-compact-convertible-avec-meridienne-dun-cote-buffet-ra-f957bac4b2e4524bcafb3b821eda0ab5.jpg?f=m 600w,
  https://www.ikea.com/images/salon-compact-convertible-avec-meridienne-dun-cote-buffet-ra-f957bac4b2e4524bcafb3b821eda0ab5.jpg?f=s 500w,
  https://www.ikea.com/images/salon-compact-convertible-avec-meridienne-dun-cote-buffet-ra-f957bac4b2e4524bcafb3b821eda0ab5.jpg?f=xs 400w,
  https://www.ikea.com/images/salon-compact-convertible-avec-meridienne-dun-cote-buffet-ra-f957bac4b2e4524bcafb3b821eda0ab5.jpg?f=xxs 300w,
  https://www.ikea.com/images/salon-compact-convertible-avec-meridienne-dun-cote-buffet-ra-f957bac4b2e4524bcafb3b821eda0ab5.jpg?f=xxxs 240w"/>
                         </span>
                        </div>
                        <div class="c1b7q3xo c8u3m6h f7zhins g1mfmhmf g5qtjc5">
                         <div class="b15fs3xm b1asp286 c30mk8n f7zhins g5qtjc5 l1rjie0o lr6adlh" style="width:100%;background-color:#e5456d">
                          <div class="bgrf0js f1dbvbh0 gd8xc1c v11tpn0s v1duoae3 gqfus6o v18by0fb">
                           <div class="">
                            <div class="gd8xc1c vmq1cv0 v18by0fb">
                             <h3 class="g2q85x8 pub__h3 s1gshh7t">
                              <div class="s1fbln9t" id="276330d0-202a-11ec-96f0-d900bf02a083-heading">
                               Un salon pour les grasses matinées
                              </div>
                             </h3>
                            </div>
                           </div>
                           <button aria-hidden="true" class="pub__btn pub__btn--icon-primary b8b8hey" tabindex="-1" type="button">
                            <span class="pub__btn__inner">
                             <svg aria-hidden="true" class="pub__svg-icon pub__btn__icon" focusable="false" viewbox="0 0 24 24">
                              <path clip-rule="evenodd" d="M19.2937 12.7074L20.0008 12.0003L19.2938 11.2932L12.0008 3.99927L10.5865 5.41339L16.1727 11.0003H4V13.0003H16.1723L10.5855 18.5868L11.9996 20.0011L19.2937 12.7074Z" fill-rule="evenodd">
                              </path>
                             </svg>
                            </span>
                           </button>
                          </div>
                         </div>
                        </div>
                       </div>
                      </a>
                     </div>
                    </div>
                   </div>
                  </div>
                 </div>
                 <button aria-controls="pub__carousel__daff86d0-2029-11ec-96f0-d900bf02a083" aria-label="Diapo suivante" class="pub__btn pub__btn--small pub__btn--icon-primary pub__carousel__button pub__carousel__button--right" id="pub__-carousel__daff86d0-2029-11ec-96f0-d900bf02a083-next-btn" type="button">
                  <span class="pub__btn__inner">
                   <svg aria-hidden="true" class="pub__svg-icon pub__btn__icon" focusable="false" viewbox="0 0 24 24">
                    <path clip-rule="evenodd" d="m16.415 12.0011-8.0012 8.0007-1.4141-1.4143 6.587-6.5866-6.586-6.5868L8.415 4l8 8.0011z" fill-rule="evenodd">
                    </path>
                   </svg>
                  </span>
                 </button>
                </div>
                <div class="pub__scroll-indicator" tabindex="0">
                </div>
                <a id="pub__-carousel__daff86d0-2029-11ec-96f0-d900bf02a083-skip-btn">
                </a>
               </div>
              </div>
             </div>
            </div>
           </div>
          </div>
         </div>
        </section>
        <section class="gd8xc1c v19w64p3 v18by0fb">
         <div id="3b31afb0-202a-11ec-96f0-d900bf02a083">
          <div class="pub__teaser t8ilr1w" data-pub-id="3b31afb0-202a-11ec-96f0-d900bf02a083" data-pub-type="product-shelf" data-use-node-click-tracking="true">
           <div class="pub__teaser__grid">
            <div class="pub__teaser__info-container">
             <div class="pub__teaser__info">
              <h2 class="pub__h2 s1gshh7t x1eq9mu0">
               Canapé le jour, lit la nuit.
              </h2>
             </div>
             <a class="pub__btn pub__btn--small pub__btn--secondary pub__teaser__top-button" href="https://www.ikea.com/ma/fr/cat/convertibles-10663/" role="button">
              <span class="pub__btn__inner">
               <span class="pub__btn__label">
                Voir tous nos convertibles
               </span>
              </span>
             </a>
            </div>
            <div class="pub__teaser__content">
             <div data-pub-hydrate="pub-carousel" data-seed='{"id":"3b31afb0-202a-11ec-96f0-d900bf02a083","prefix":"pub__","contentClass":"c9nzkp0","itemClass":"ixrpjrm","rtl":false}' style="height:100%">
              <div class="pub__carousel" tabindex="-1">
               <a class="btn btn--primary-inverse pub__carousel__skip-button" href="#pub__-carousel__3b31afb0-202a-11ec-96f0-d900bf02a083-skip-btn" role="button">
                <span class="btn__inner">
                 Skip listing
                </span>
               </a>
               <div class="pub__carousel__wrapper">
                <button aria-controls="pub__carousel__3b31afb0-202a-11ec-96f0-d900bf02a083" aria-label="See previous items" class="pub__btn pub__btn--small pub__btn--icon-primary pub__carousel__button" id="pub__-carousel__3b31afb0-202a-11ec-96f0-d900bf02a083-prev-btn" type="button">
                 <span class="pub__btn__inner">
                  <svg aria-hidden="true" class="pub__svg-icon pub__btn__icon" focusable="false" viewbox="0 0 24 24">
                   <path clip-rule="evenodd" d="m7 12.0009 8.0012-8.0007 1.4142 1.4142-6.587 6.5866 6.5859 6.5868L15 20.002l-8-8.0011z" fill-rule="evenodd">
                   </path>
                  </svg>
                 </span>
                </button>
                <div class="pub__carousel__content c9nzkp0 pub__carousel__content--snap-slide">
                 <div class="pub__carousel__body-wrapper">
                  <div class="pub__carousel__body" id="pub__carousel__3b31afb0-202a-11ec-96f0-d900bf02a083">
                   <div class="pub__carousel-slide ixrpjrm">
                    <div data-pub-hydrate-child="pub-carousel">
                     <div class="range-revamp-product-compact" data-cs-capture="" data-currency="MAD" data-price="5995" data-product-compact="" data-product-name="FRIHETEN" data-product-number="39216754" data-product-type="SPR" data-ref-id="39216754">
                      <button aria-label="Ajouter à mes favoris" aria-pressed="false" class="range-revamp-toggle-button range-revamp-toggle-button--icon-only range-revamp-toggle-button--transparent range-revamp-product-compact__add-to-list-button">
                       <svg aria-hidden="true" class="range-revamp-svg-icon" focusable="false" viewbox="0 0 24 24">
                        <path clip-rule="evenodd" d="M12.336 5.52055C14.2336 3.62376 17.3096 3.62401 19.2069 5.52129C20.2067 6.52115 20.6796 7.85005 20.6259 9.15761C20.6151 12.2138 18.4184 14.8654 16.4892 16.6366C15.4926 17.5517 14.5004 18.2923 13.7593 18.8036C13.3879 19.0598 13.0771 19.2601 12.8574 19.3973C12.7475 19.466 12.6601 19.519 12.5992 19.5555C12.5687 19.5737 12.5448 19.5879 12.5279 19.5978L12.5079 19.6094L12.502 19.6129L12.5001 19.614C12.5001 19.614 12.4989 19.6147 11.9999 18.748C11.501 19.6147 11.5005 19.6144 11.5005 19.6144L11.4979 19.6129L11.4919 19.6094L11.472 19.5978C11.4551 19.5879 11.4312 19.5737 11.4007 19.5555C11.3397 19.519 11.2524 19.466 11.1425 19.3973C10.9227 19.2601 10.612 19.0598 10.2405 18.8036C9.49947 18.2923 8.50726 17.5517 7.51063 16.6366C5.58146 14.8654 3.38477 12.2139 3.37399 9.15765C3.32024 7.85008 3.79314 6.52117 4.79301 5.52129C6.69054 3.62376 9.76704 3.62376 11.6646 5.52129L11.9993 5.856L12.3353 5.52129L12.336 5.52055ZM11.9999 18.748L11.5005 19.6144L11.9999 19.9019L12.4989 19.6147L11.9999 18.748ZM11.9999 17.573C12.1727 17.462 12.384 17.3226 12.6236 17.1573C13.3125 16.6821 14.2267 15.9988 15.1366 15.1634C17.0157 13.4381 18.6259 11.2919 18.6259 9.13506V9.11213L18.627 9.08922C18.6626 8.31221 18.3844 7.52727 17.7926 6.9355C16.6762 5.81903 14.866 5.81902 13.7495 6.9355L13.7481 6.93689L11.9965 8.68166L10.2504 6.9355C9.13387 5.81903 7.3237 5.81903 6.20722 6.9355C5.61546 7.52727 5.33724 8.31221 5.3729 9.08922L5.37395 9.11213V9.13507C5.37395 11.2919 6.98418 13.4381 8.86325 15.1634C9.77312 15.9988 10.6874 16.6821 11.3762 17.1573C11.6159 17.3226 11.8271 17.462 11.9999 17.573Z" fill-rule="evenodd">
                        </path>
                       </svg>
                      </button>
                      <a aria-label="FRIHETEN - Canapé convertible angle+rangement" href="https://www.ikea.com/ma/fr/p/friheten-canape-convertible-angle-rangement-skiftebo-gris-fonce-s39216754/">
                       <div class="range-revamp-product-compact__image-wrapper">
                        <span class="range-revamp-aspect-ratio-image range-revamp-aspect-ratio-image--square">
                         <img alt="FRIHETEN Canapé convertible angle+rangement, Skiftebo gris foncé" class="range-revamp-aspect-ratio-image__image" loading="lazy" sizes="(max-width: 400px) 80px, (max-width: 1450px) 160px, 300px" src="https://www.ikea.com/ma/fr/images/products/friheten-corner-sofa-bed-with-storage-skiftebo-dark-grey__0175610_pe328883_s5.jpg?f=xxs" srcset="
      https://www.ikea.com/ma/fr/images/products/friheten-corner-sofa-bed-with-storage-skiftebo-dark-grey__0175610_pe328883_s5.jpg?f=m 600w,
      https://www.ikea.com/ma/fr/images/products/friheten-corner-sofa-bed-with-storage-skiftebo-dark-grey__0175610_pe328883_s5.jpg?f=xxs 300w,
      https://www.ikea.com/ma/fr/images/products/friheten-corner-sofa-bed-with-storage-skiftebo-dark-grey__0175610_pe328883_s5.jpg?f=xxxs 160w,
      https://www.ikea.com/ma/fr/images/products/friheten-corner-sofa-bed-with-storage-skiftebo-dark-grey__0175610_pe328883_s5.jpg?f=u 80w
      "/>
                        </span>
                        <span class="range-revamp-aspect-ratio-image range-revamp-aspect-ratio-image--square range-revamp-product-compact__image-hover range-revamp-product-compact__image-hover--inactive">
                         <img alt="" class="range-revamp-aspect-ratio-image__image" data-src="https://www.ikea.com/ma/fr/images/products/friheten-corner-sofa-bed-with-storage-skiftebo-dark-grey__0833845_pe603738_s5.jpg?f=xxs" data-src-set="
      https://www.ikea.com/ma/fr/images/products/friheten-corner-sofa-bed-with-storage-skiftebo-dark-grey__0833845_pe603738_s5.jpg?f=m 600w,
      https://www.ikea.com/ma/fr/images/products/friheten-corner-sofa-bed-with-storage-skiftebo-dark-grey__0833845_pe603738_s5.jpg?f=xxs 300w,
      https://www.ikea.com/ma/fr/images/products/friheten-corner-sofa-bed-with-storage-skiftebo-dark-grey__0833845_pe603738_s5.jpg?f=xxxs 160w,
      https://www.ikea.com/ma/fr/images/products/friheten-corner-sofa-bed-with-storage-skiftebo-dark-grey__0833845_pe603738_s5.jpg?f=u 80w
      " loading="lazy" sizes="(max-width: 400px) 80px, (max-width: 1450px) 160px, 300px" src="data:image/gif;base64,R0lGODdhAQABAIAAAP///wAAACwAAAAAAQABAAACAkQBADs=" srcset=""/>
                        </span>
                       </div>
                      </a>
                      <div class="range-revamp-product-compact__bottom-wrapper">
                       <a class="range-revamp-product-compact__wrapper-link" href="https://www.ikea.com/ma/fr/p/friheten-canape-convertible-angle-rangement-skiftebo-gris-fonce-s39216754/">
                        <div class="range-revamp-compact-price-package">
                         <div class="range-revamp-compact-price-package__additional-info">
                          <div class="range-revamp-header-section">
                           <div class="range-revamp-header-section__title--small notranslate">
                            FRIHETEN
                           </div>
                           <div class="range-revamp-header-section__description">
                            <span class="range-revamp-header-section__description-text">
                             Canapé convertible angle+rangement
                            </span>
                           </div>
                          </div>
                         </div>
                         <div class="range-revamp-compact-price-package__previous-price-wrapper">
                         </div>
                         <div class="range-revamp-compact-price-package__price-wrapper">
                          <span class="range-revamp-price">
                           <span class="range-revamp-price__integer">
                            5 995
                           </span>
                           <span class="range-revamp-price__currency-symbol range-revamp-price__currency-symbol--trailing range-revamp-price__currency-symbol--superscript">
                            DH
                           </span>
                          </span>
                         </div>
                         <span class="range-revamp-compact-price-package__variations-disclaimer" data-product-compact-gpr="">
                          Plus d'options
                         </span>
                        </div>
                       </a>
                      </div>
                     </div>
                    </div>
                   </div>
                   <div class="pub__carousel-slide ixrpjrm">
                    <div data-pub-hydrate-child="pub-carousel">
                     <div class="range-revamp-product-compact" data-cs-capture="" data-currency="MAD" data-price="3695" data-product-compact="" data-product-name="NYHAMN" data-product-number="39306368" data-product-type="SPR" data-ref-id="39306368">
                      <button aria-label="Ajouter à mes favoris" aria-pressed="false" class="range-revamp-toggle-button range-revamp-toggle-button--icon-only range-revamp-toggle-button--transparent range-revamp-product-compact__add-to-list-button">
                       <svg aria-hidden="true" class="range-revamp-svg-icon" focusable="false" viewbox="0 0 24 24">
                        <path clip-rule="evenodd" d="M12.336 5.52055C14.2336 3.62376 17.3096 3.62401 19.2069 5.52129C20.2067 6.52115 20.6796 7.85005 20.6259 9.15761C20.6151 12.2138 18.4184 14.8654 16.4892 16.6366C15.4926 17.5517 14.5004 18.2923 13.7593 18.8036C13.3879 19.0598 13.0771 19.2601 12.8574 19.3973C12.7475 19.466 12.6601 19.519 12.5992 19.5555C12.5687 19.5737 12.5448 19.5879 12.5279 19.5978L12.5079 19.6094L12.502 19.6129L12.5001 19.614C12.5001 19.614 12.4989 19.6147 11.9999 18.748C11.501 19.6147 11.5005 19.6144 11.5005 19.6144L11.4979 19.6129L11.4919 19.6094L11.472 19.5978C11.4551 19.5879 11.4312 19.5737 11.4007 19.5555C11.3397 19.519 11.2524 19.466 11.1425 19.3973C10.9227 19.2601 10.612 19.0598 10.2405 18.8036C9.49947 18.2923 8.50726 17.5517 7.51063 16.6366C5.58146 14.8654 3.38477 12.2139 3.37399 9.15765C3.32024 7.85008 3.79314 6.52117 4.79301 5.52129C6.69054 3.62376 9.76704 3.62376 11.6646 5.52129L11.9993 5.856L12.3353 5.52129L12.336 5.52055ZM11.9999 18.748L11.5005 19.6144L11.9999 19.9019L12.4989 19.6147L11.9999 18.748ZM11.9999 17.573C12.1727 17.462 12.384 17.3226 12.6236 17.1573C13.3125 16.6821 14.2267 15.9988 15.1366 15.1634C17.0157 13.4381 18.6259 11.2919 18.6259 9.13506V9.11213L18.627 9.08922C18.6626 8.31221 18.3844 7.52727 17.7926 6.9355C16.6762 5.81903 14.866 5.81902 13.7495 6.9355L13.7481 6.93689L11.9965 8.68166L10.2504 6.9355C9.13387 5.81903 7.3237 5.81903 6.20722 6.9355C5.61546 7.52727 5.33724 8.31221 5.3729 9.08922L5.37395 9.11213V9.13507C5.37395 11.2919 6.98418 13.4381 8.86325 15.1634C9.77312 15.9988 10.6874 16.6821 11.3762 17.1573C11.6159 17.3226 11.8271 17.462 11.9999 17.573Z" fill-rule="evenodd">
                        </path>
                       </svg>
                      </button>
                      <a aria-label="NYHAMN - Canapé 3 places convertible" href="https://www.ikea.com/ma/fr/p/nyhamn-canape-3-places-convertible-avec-matelas-en-mousse-knisa-gris-beige-s39306368/">
                       <div class="range-revamp-product-compact__image-wrapper">
                        <span class="range-revamp-aspect-ratio-image range-revamp-aspect-ratio-image--square">
                         <img alt="NYHAMN Canapé 3 places convertible, avec matelas en mousse/Knisa gris/beige" class="range-revamp-aspect-ratio-image__image" loading="lazy" sizes="(max-width: 400px) 80px, (max-width: 1450px) 160px, 300px" src="https://www.ikea.com/ma/fr/images/products/nyhamn-3-seat-sofa-bed-with-foam-mattress-knisa-grey-beige__0767330_pe754069_s5.jpg?f=xxs" srcset="
      https://www.ikea.com/ma/fr/images/products/nyhamn-3-seat-sofa-bed-with-foam-mattress-knisa-grey-beige__0767330_pe754069_s5.jpg?f=m 600w,
      https://www.ikea.com/ma/fr/images/products/nyhamn-3-seat-sofa-bed-with-foam-mattress-knisa-grey-beige__0767330_pe754069_s5.jpg?f=xxs 300w,
      https://www.ikea.com/ma/fr/images/products/nyhamn-3-seat-sofa-bed-with-foam-mattress-knisa-grey-beige__0767330_pe754069_s5.jpg?f=xxxs 160w,
      https://www.ikea.com/ma/fr/images/products/nyhamn-3-seat-sofa-bed-with-foam-mattress-knisa-grey-beige__0767330_pe754069_s5.jpg?f=u 80w
      "/>
                        </span>
                        <span class="range-revamp-aspect-ratio-image range-revamp-aspect-ratio-image--square range-revamp-product-compact__image-hover range-revamp-product-compact__image-hover--inactive">
                         <img alt="" class="range-revamp-aspect-ratio-image__image" data-src="https://www.ikea.com/ma/fr/images/products/nyhamn-3-seat-sofa-bed-with-foam-mattress-knisa-grey-beige__0767327_pe754068_s5.jpg?f=xxs" data-src-set="
      https://www.ikea.com/ma/fr/images/products/nyhamn-3-seat-sofa-bed-with-foam-mattress-knisa-grey-beige__0767327_pe754068_s5.jpg?f=m 600w,
      https://www.ikea.com/ma/fr/images/products/nyhamn-3-seat-sofa-bed-with-foam-mattress-knisa-grey-beige__0767327_pe754068_s5.jpg?f=xxs 300w,
      https://www.ikea.com/ma/fr/images/products/nyhamn-3-seat-sofa-bed-with-foam-mattress-knisa-grey-beige__0767327_pe754068_s5.jpg?f=xxxs 160w,
      https://www.ikea.com/ma/fr/images/products/nyhamn-3-seat-sofa-bed-with-foam-mattress-knisa-grey-beige__0767327_pe754068_s5.jpg?f=u 80w
      " loading="lazy" sizes="(max-width: 400px) 80px, (max-width: 1450px) 160px, 300px" src="data:image/gif;base64,R0lGODdhAQABAIAAAP///wAAACwAAAAAAQABAAACAkQBADs=" srcset=""/>
                        </span>
                       </div>
                      </a>
                      <div class="range-revamp-product-compact__bottom-wrapper">
                       <a class="range-revamp-product-compact__wrapper-link" href="https://www.ikea.com/ma/fr/p/nyhamn-canape-3-places-convertible-avec-matelas-en-mousse-knisa-gris-beige-s39306368/">
                        <div class="range-revamp-compact-price-package">
                         <div class="range-revamp-compact-price-package__additional-info">
                          <div class="range-revamp-header-section">
                           <div class="range-revamp-header-section__title--small notranslate">
                            NYHAMN
                           </div>
                           <div class="range-revamp-header-section__description">
                            <span class="range-revamp-header-section__description-text">
                             Canapé 3 places convertible
                            </span>
                           </div>
                          </div>
                         </div>
                         <div class="range-revamp-compact-price-package__previous-price-wrapper">
                         </div>
                         <div class="range-revamp-compact-price-package__price-wrapper">
                          <span class="range-revamp-price">
                           <span class="range-revamp-price__integer">
                            3 695
                           </span>
                           <span class="range-revamp-price__currency-symbol range-revamp-price__currency-symbol--trailing range-revamp-price__currency-symbol--superscript">
                            DH
                           </span>
                          </span>
                         </div>
                         <span class="range-revamp-compact-price-package__last-chance">
                          Dernière chance d'achat
                         </span>
                         <span class="range-revamp-compact-price-package__variations-disclaimer" data-product-compact-gpr="">
                          Plus d'options
                         </span>
                        </div>
                       </a>
                       <button aria-label="Achetez En ligne" class="range-revamp-btn range-revamp-btn--small range-revamp-btn--icon-emphasised range-revamp-product-compact__add-to-cart-button" type="button">
                        <span class="range-revamp-btn__inner">
                         <svg aria-hidden="true" class="range-revamp-svg-icon range-revamp-btn__icon" focusable="false" viewbox="0 0 24 24">
                          <path clip-rule="evenodd" d="M10.4372 4H10.9993H12.0003H12.9996H13.5616L13.8538 4.48014L17.2112 9.99713H21H22.2806L21.9702 11.2396L21.5303 13H19.4688L19.7194 11.9971H4.28079L5.59143 17.2397C5.70272 17.6848 6.1027 17.9971 6.56157 17.9971H15V19.9971H6.56157C5.18496 19.9971 3.98502 19.0602 3.65114 17.7247L2.02987 11.2397L1.71924 9.99713H3.00002H6.78793L10.145 4.48017L10.4372 4ZM12.4375 6L14.87 9.99713H9.12911L11.5614 6H12.0003H12.4375ZM17.9961 16V14H19.9961V16H21.9961V18H19.9961V20H17.9961V18H15.9961V16H17.9961Z" fill-rule="evenodd">
                          </path>
                         </svg>
                        </span>
                       </button>
                      </div>
                     </div>
                    </div>
                   </div>
                   <div class="pub__carousel-slide ixrpjrm">
                    <div data-pub-hydrate-child="pub-carousel">
                     <div class="range-revamp-product-compact" data-cs-capture="" data-currency="MAD" data-price="3495" data-product-compact="" data-product-name="LYCKSELE LÖVÅS" data-product-number="99387007" data-product-type="SPR" data-ref-id="99387007">
                      <button aria-label="Ajouter à mes favoris" aria-pressed="false" class="range-revamp-toggle-button range-revamp-toggle-button--icon-only range-revamp-toggle-button--transparent range-revamp-product-compact__add-to-list-button">
                       <svg aria-hidden="true" class="range-revamp-svg-icon" focusable="false" viewbox="0 0 24 24">
                        <path clip-rule="evenodd" d="M12.336 5.52055C14.2336 3.62376 17.3096 3.62401 19.2069 5.52129C20.2067 6.52115 20.6796 7.85005 20.6259 9.15761C20.6151 12.2138 18.4184 14.8654 16.4892 16.6366C15.4926 17.5517 14.5004 18.2923 13.7593 18.8036C13.3879 19.0598 13.0771 19.2601 12.8574 19.3973C12.7475 19.466 12.6601 19.519 12.5992 19.5555C12.5687 19.5737 12.5448 19.5879 12.5279 19.5978L12.5079 19.6094L12.502 19.6129L12.5001 19.614C12.5001 19.614 12.4989 19.6147 11.9999 18.748C11.501 19.6147 11.5005 19.6144 11.5005 19.6144L11.4979 19.6129L11.4919 19.6094L11.472 19.5978C11.4551 19.5879 11.4312 19.5737 11.4007 19.5555C11.3397 19.519 11.2524 19.466 11.1425 19.3973C10.9227 19.2601 10.612 19.0598 10.2405 18.8036C9.49947 18.2923 8.50726 17.5517 7.51063 16.6366C5.58146 14.8654 3.38477 12.2139 3.37399 9.15765C3.32024 7.85008 3.79314 6.52117 4.79301 5.52129C6.69054 3.62376 9.76704 3.62376 11.6646 5.52129L11.9993 5.856L12.3353 5.52129L12.336 5.52055ZM11.9999 18.748L11.5005 19.6144L11.9999 19.9019L12.4989 19.6147L11.9999 18.748ZM11.9999 17.573C12.1727 17.462 12.384 17.3226 12.6236 17.1573C13.3125 16.6821 14.2267 15.9988 15.1366 15.1634C17.0157 13.4381 18.6259 11.2919 18.6259 9.13506V9.11213L18.627 9.08922C18.6626 8.31221 18.3844 7.52727 17.7926 6.9355C16.6762 5.81903 14.866 5.81902 13.7495 6.9355L13.7481 6.93689L11.9965 8.68166L10.2504 6.9355C9.13387 5.81903 7.3237 5.81903 6.20722 6.9355C5.61546 7.52727 5.33724 8.31221 5.3729 9.08922L5.37395 9.11213V9.13507C5.37395 11.2919 6.98418 13.4381 8.86325 15.1634C9.77312 15.9988 10.6874 16.6821 11.3762 17.1573C11.6159 17.3226 11.8271 17.462 11.9999 17.573Z" fill-rule="evenodd">
                        </path>
                       </svg>
                      </button>
                      <a aria-label="LYCKSELE LÖVÅS - Convertible 2 places" href="https://www.ikea.com/ma/fr/p/lycksele-loevas-convertible-2-places-ransta-naturel-s99387007/">
                       <div class="range-revamp-product-compact__image-wrapper">
                        <span class="range-revamp-aspect-ratio-image range-revamp-aspect-ratio-image--square">
                         <img alt="LYCKSELE LÖVÅS Convertible 2 places, Ransta naturel" class="range-revamp-aspect-ratio-image__image" loading="lazy" sizes="(max-width: 400px) 80px, (max-width: 1450px) 160px, 300px" src="https://www.ikea.com/ma/fr/images/products/lycksele-loevas-2-seat-sofa-bed-ransta-natural__0949712_pe799986_s5.jpg?f=xxs" srcset="
      https://www.ikea.com/ma/fr/images/products/lycksele-loevas-2-seat-sofa-bed-ransta-natural__0949712_pe799986_s5.jpg?f=m 600w,
      https://www.ikea.com/ma/fr/images/products/lycksele-loevas-2-seat-sofa-bed-ransta-natural__0949712_pe799986_s5.jpg?f=xxs 300w,
      https://www.ikea.com/ma/fr/images/products/lycksele-loevas-2-seat-sofa-bed-ransta-natural__0949712_pe799986_s5.jpg?f=xxxs 160w,
      https://www.ikea.com/ma/fr/images/products/lycksele-loevas-2-seat-sofa-bed-ransta-natural__0949712_pe799986_s5.jpg?f=u 80w
      "/>
                        </span>
                        <span class="range-revamp-aspect-ratio-image range-revamp-aspect-ratio-image--square range-revamp-product-compact__image-hover range-revamp-product-compact__image-hover--inactive">
                         <img alt="" class="range-revamp-aspect-ratio-image__image" data-src="https://www.ikea.com/ma/fr/images/products/lycksele-loevas-2-seat-sofa-bed-ransta-natural__0949714_pe799974_s5.jpg?f=xxs" data-src-set="
      https://www.ikea.com/ma/fr/images/products/lycksele-loevas-2-seat-sofa-bed-ransta-natural__0949714_pe799974_s5.jpg?f=m 600w,
      https://www.ikea.com/ma/fr/images/products/lycksele-loevas-2-seat-sofa-bed-ransta-natural__0949714_pe799974_s5.jpg?f=xxs 300w,
      https://www.ikea.com/ma/fr/images/products/lycksele-loevas-2-seat-sofa-bed-ransta-natural__0949714_pe799974_s5.jpg?f=xxxs 160w,
      https://www.ikea.com/ma/fr/images/products/lycksele-loevas-2-seat-sofa-bed-ransta-natural__0949714_pe799974_s5.jpg?f=u 80w
      " loading="lazy" sizes="(max-width: 400px) 80px, (max-width: 1450px) 160px, 300px" src="data:image/gif;base64,R0lGODdhAQABAIAAAP///wAAACwAAAAAAQABAAACAkQBADs=" srcset=""/>
                        </span>
                       </div>
                      </a>
                      <div class="range-revamp-product-compact__bottom-wrapper">
                       <a class="range-revamp-product-compact__wrapper-link" href="https://www.ikea.com/ma/fr/p/lycksele-loevas-convertible-2-places-ransta-naturel-s99387007/">
                        <div class="range-revamp-compact-price-package">
                         <div class="range-revamp-compact-price-package__additional-info">
                          <div class="range-revamp-header-section">
                           <div class="range-revamp-header-section__title--small notranslate">
                            LYCKSELE LÖVÅS
                           </div>
                           <div class="range-revamp-header-section__description">
                            <span class="range-revamp-header-section__description-text">
                             Convertible 2 places
                            </span>
                           </div>
                          </div>
                         </div>
                         <div class="range-revamp-compact-price-package__previous-price-wrapper">
                         </div>
                         <div class="range-revamp-compact-price-package__price-wrapper">
                          <span class="range-revamp-price">
                           <span class="range-revamp-price__integer">
                            3 495
                           </span>
                           <span class="range-revamp-price__currency-symbol range-revamp-price__currency-symbol--trailing range-revamp-price__currency-symbol--superscript">
                            DH
                           </span>
                          </span>
                         </div>
                         <span class="range-revamp-compact-price-package__variations-disclaimer" data-product-compact-gpr="">
                          Plus d'options
                         </span>
                        </div>
                       </a>
                       <button aria-label="Achetez En ligne" class="range-revamp-btn range-revamp-btn--small range-revamp-btn--icon-emphasised range-revamp-product-compact__add-to-cart-button" type="button">
                        <span class="range-revamp-btn__inner">
                         <svg aria-hidden="true" class="range-revamp-svg-icon range-revamp-btn__icon" focusable="false" viewbox="0 0 24 24">
                          <path clip-rule="evenodd" d="M10.4372 4H10.9993H12.0003H12.9996H13.5616L13.8538 4.48014L17.2112 9.99713H21H22.2806L21.9702 11.2396L21.5303 13H19.4688L19.7194 11.9971H4.28079L5.59143 17.2397C5.70272 17.6848 6.1027 17.9971 6.56157 17.9971H15V19.9971H6.56157C5.18496 19.9971 3.98502 19.0602 3.65114 17.7247L2.02987 11.2397L1.71924 9.99713H3.00002H6.78793L10.145 4.48017L10.4372 4ZM12.4375 6L14.87 9.99713H9.12911L11.5614 6H12.0003H12.4375ZM17.9961 16V14H19.9961V16H21.9961V18H19.9961V20H17.9961V18H15.9961V16H17.9961Z" fill-rule="evenodd">
                          </path>
                         </svg>
                        </span>
                       </button>
                      </div>
                     </div>
                    </div>
                   </div>
                   <div class="pub__carousel-slide ixrpjrm">
                    <div data-pub-hydrate-child="pub-carousel">
                     <div class="range-revamp-product-compact" data-cs-capture="" data-currency="MAD" data-price="8195" data-product-compact="" data-product-name="HOLMSUND" data-product-number="29228205" data-product-type="SPR" data-ref-id="29228205">
                      <button aria-label="Ajouter à mes favoris" aria-pressed="false" class="range-revamp-toggle-button range-revamp-toggle-button--icon-only range-revamp-toggle-button--transparent range-revamp-product-compact__add-to-list-button">
                       <svg aria-hidden="true" class="range-revamp-svg-icon" focusable="false" viewbox="0 0 24 24">
                        <path clip-rule="evenodd" d="M12.336 5.52055C14.2336 3.62376 17.3096 3.62401 19.2069 5.52129C20.2067 6.52115 20.6796 7.85005 20.6259 9.15761C20.6151 12.2138 18.4184 14.8654 16.4892 16.6366C15.4926 17.5517 14.5004 18.2923 13.7593 18.8036C13.3879 19.0598 13.0771 19.2601 12.8574 19.3973C12.7475 19.466 12.6601 19.519 12.5992 19.5555C12.5687 19.5737 12.5448 19.5879 12.5279 19.5978L12.5079 19.6094L12.502 19.6129L12.5001 19.614C12.5001 19.614 12.4989 19.6147 11.9999 18.748C11.501 19.6147 11.5005 19.6144 11.5005 19.6144L11.4979 19.6129L11.4919 19.6094L11.472 19.5978C11.4551 19.5879 11.4312 19.5737 11.4007 19.5555C11.3397 19.519 11.2524 19.466 11.1425 19.3973C10.9227 19.2601 10.612 19.0598 10.2405 18.8036C9.49947 18.2923 8.50726 17.5517 7.51063 16.6366C5.58146 14.8654 3.38477 12.2139 3.37399 9.15765C3.32024 7.85008 3.79314 6.52117 4.79301 5.52129C6.69054 3.62376 9.76704 3.62376 11.6646 5.52129L11.9993 5.856L12.3353 5.52129L12.336 5.52055ZM11.9999 18.748L11.5005 19.6144L11.9999 19.9019L12.4989 19.6147L11.9999 18.748ZM11.9999 17.573C12.1727 17.462 12.384 17.3226 12.6236 17.1573C13.3125 16.6821 14.2267 15.9988 15.1366 15.1634C17.0157 13.4381 18.6259 11.2919 18.6259 9.13506V9.11213L18.627 9.08922C18.6626 8.31221 18.3844 7.52727 17.7926 6.9355C16.6762 5.81903 14.866 5.81902 13.7495 6.9355L13.7481 6.93689L11.9965 8.68166L10.2504 6.9355C9.13387 5.81903 7.3237 5.81903 6.20722 6.9355C5.61546 7.52727 5.33724 8.31221 5.3729 9.08922L5.37395 9.11213V9.13507C5.37395 11.2919 6.98418 13.4381 8.86325 15.1634C9.77312 15.9988 10.6874 16.6821 11.3762 17.1573C11.6159 17.3226 11.8271 17.462 11.9999 17.573Z" fill-rule="evenodd">
                        </path>
                       </svg>
                      </button>
                      <a aria-label="HOLMSUND - Canapé convertible d'angle" href="https://www.ikea.com/ma/fr/p/holmsund-canape-convertible-dangle-orrsta-bleu-clair-s29228205/">
                       <div class="range-revamp-product-compact__image-wrapper">
                        <span class="range-revamp-aspect-ratio-image range-revamp-aspect-ratio-image--square">
                         <img alt="HOLMSUND Canapé convertible d'angle, Orrsta bleu clair" class="range-revamp-aspect-ratio-image__image" loading="lazy" sizes="(max-width: 400px) 80px, (max-width: 1450px) 160px, 300px" src="https://www.ikea.com/ma/fr/images/products/holmsund-corner-sofa-bed-orrsta-light-blue__0532354_pe648004_s5.jpg?f=xxs" srcset="
      https://www.ikea.com/ma/fr/images/products/holmsund-corner-sofa-bed-orrsta-light-blue__0532354_pe648004_s5.jpg?f=m 600w,
      https://www.ikea.com/ma/fr/images/products/holmsund-corner-sofa-bed-orrsta-light-blue__0532354_pe648004_s5.jpg?f=xxs 300w,
      https://www.ikea.com/ma/fr/images/products/holmsund-corner-sofa-bed-orrsta-light-blue__0532354_pe648004_s5.jpg?f=xxxs 160w,
      https://www.ikea.com/ma/fr/images/products/holmsund-corner-sofa-bed-orrsta-light-blue__0532354_pe648004_s5.jpg?f=u 80w
      "/>
                        </span>
                        <span class="range-revamp-aspect-ratio-image range-revamp-aspect-ratio-image--square range-revamp-product-compact__image-hover range-revamp-product-compact__image-hover--inactive">
                         <img alt="" class="range-revamp-aspect-ratio-image__image" data-src="https://www.ikea.com/ma/fr/images/products/holmsund-corner-sofa-bed-orrsta-light-blue__0828571_pe648005_s5.jpg?f=xxs" data-src-set="
      https://www.ikea.com/ma/fr/images/products/holmsund-corner-sofa-bed-orrsta-light-blue__0828571_pe648005_s5.jpg?f=m 600w,
      https://www.ikea.com/ma/fr/images/products/holmsund-corner-sofa-bed-orrsta-light-blue__0828571_pe648005_s5.jpg?f=xxs 300w,
      https://www.ikea.com/ma/fr/images/products/holmsund-corner-sofa-bed-orrsta-light-blue__0828571_pe648005_s5.jpg?f=xxxs 160w,
      https://www.ikea.com/ma/fr/images/products/holmsund-corner-sofa-bed-orrsta-light-blue__0828571_pe648005_s5.jpg?f=u 80w
      " loading="lazy" sizes="(max-width: 400px) 80px, (max-width: 1450px) 160px, 300px" src="data:image/gif;base64,R0lGODdhAQABAIAAAP///wAAACwAAAAAAQABAAACAkQBADs=" srcset=""/>
                        </span>
                       </div>
                      </a>
                      <div class="range-revamp-product-compact__bottom-wrapper">
                       <a class="range-revamp-product-compact__wrapper-link" href="https://www.ikea.com/ma/fr/p/holmsund-canape-convertible-dangle-orrsta-bleu-clair-s29228205/">
                        <div class="range-revamp-compact-price-package">
                         <div class="range-revamp-compact-price-package__additional-info">
                          <div class="range-revamp-header-section">
                           <div class="range-revamp-header-section__title--small notranslate">
                            HOLMSUND
                           </div>
                           <div class="range-revamp-header-section__description">
                            <span class="range-revamp-header-section__description-text">
                             Canapé convertible d'angle
                            </span>
                           </div>
                          </div>
                         </div>
                         <div class="range-revamp-compact-price-package__previous-price-wrapper">
                         </div>
                         <div class="range-revamp-compact-price-package__price-wrapper">
                          <span class="range-revamp-price">
                           <span class="range-revamp-price__integer">
                            8 195
                           </span>
                           <span class="range-revamp-price__currency-symbol range-revamp-price__currency-symbol--trailing range-revamp-price__currency-symbol--superscript">
                            DH
                           </span>
                          </span>
                         </div>
                         <span class="range-revamp-compact-price-package__variations-disclaimer" data-product-compact-gpr="">
                          Plus d'options
                         </span>
                        </div>
                       </a>
                      </div>
                     </div>
                    </div>
                   </div>
                   <div class="pub__carousel-slide ixrpjrm">
                    <div data-pub-hydrate-child="pub-carousel">
                     <span class="product-missing">
                     </span>
                    </div>
                   </div>
                   <div class="pub__carousel-slide ixrpjrm">
                    <div data-pub-hydrate-child="pub-carousel">
                     <div class="range-revamp-product-compact" data-cs-capture="" data-currency="MAD" data-price="8390" data-product-compact="" data-product-name="VALLENTUNA" data-product-number="79396442" data-product-type="SPR" data-ref-id="79396442">
                      <button aria-label="Ajouter à mes favoris" aria-pressed="false" class="range-revamp-toggle-button range-revamp-toggle-button--icon-only range-revamp-toggle-button--transparent range-revamp-product-compact__add-to-list-button">
                       <svg aria-hidden="true" class="range-revamp-svg-icon" focusable="false" viewbox="0 0 24 24">
                        <path clip-rule="evenodd" d="M12.336 5.52055C14.2336 3.62376 17.3096 3.62401 19.2069 5.52129C20.2067 6.52115 20.6796 7.85005 20.6259 9.15761C20.6151 12.2138 18.4184 14.8654 16.4892 16.6366C15.4926 17.5517 14.5004 18.2923 13.7593 18.8036C13.3879 19.0598 13.0771 19.2601 12.8574 19.3973C12.7475 19.466 12.6601 19.519 12.5992 19.5555C12.5687 19.5737 12.5448 19.5879 12.5279 19.5978L12.5079 19.6094L12.502 19.6129L12.5001 19.614C12.5001 19.614 12.4989 19.6147 11.9999 18.748C11.501 19.6147 11.5005 19.6144 11.5005 19.6144L11.4979 19.6129L11.4919 19.6094L11.472 19.5978C11.4551 19.5879 11.4312 19.5737 11.4007 19.5555C11.3397 19.519 11.2524 19.466 11.1425 19.3973C10.9227 19.2601 10.612 19.0598 10.2405 18.8036C9.49947 18.2923 8.50726 17.5517 7.51063 16.6366C5.58146 14.8654 3.38477 12.2139 3.37399 9.15765C3.32024 7.85008 3.79314 6.52117 4.79301 5.52129C6.69054 3.62376 9.76704 3.62376 11.6646 5.52129L11.9993 5.856L12.3353 5.52129L12.336 5.52055ZM11.9999 18.748L11.5005 19.6144L11.9999 19.9019L12.4989 19.6147L11.9999 18.748ZM11.9999 17.573C12.1727 17.462 12.384 17.3226 12.6236 17.1573C13.3125 16.6821 14.2267 15.9988 15.1366 15.1634C17.0157 13.4381 18.6259 11.2919 18.6259 9.13506V9.11213L18.627 9.08922C18.6626 8.31221 18.3844 7.52727 17.7926 6.9355C16.6762 5.81903 14.866 5.81902 13.7495 6.9355L13.7481 6.93689L11.9965 8.68166L10.2504 6.9355C9.13387 5.81903 7.3237 5.81903 6.20722 6.9355C5.61546 7.52727 5.33724 8.31221 5.3729 9.08922L5.37395 9.11213V9.13507C5.37395 11.2919 6.98418 13.4381 8.86325 15.1634C9.77312 15.9988 10.6874 16.6821 11.3762 17.1573C11.6159 17.3226 11.8271 17.462 11.9999 17.573Z" fill-rule="evenodd">
                        </path>
                       </svg>
                      </button>
                      <a aria-label="VALLENTUNA - Module convertible avec dossiers" href="https://www.ikea.com/ma/fr/p/vallentuna-module-convertible-avec-dossiers-kelinge-rouille-s79396442/">
                       <div class="range-revamp-product-compact__image-wrapper">
                        <span class="range-revamp-aspect-ratio-image range-revamp-aspect-ratio-image--square">
                         <img alt="VALLENTUNA Module convertible avec dossiers, Kelinge rouille" class="range-revamp-aspect-ratio-image__image" loading="lazy" sizes="(max-width: 400px) 80px, (max-width: 1450px) 160px, 300px" src="https://www.ikea.com/ma/fr/images/products/vallentuna-sofa-bed-module-with-backrests-kelinge-rust__0938369_pe794076_s5.jpg?f=xxs" srcset="
      https://www.ikea.com/ma/fr/images/products/vallentuna-sofa-bed-module-with-backrests-kelinge-rust__0938369_pe794076_s5.jpg?f=m 600w,
      https://www.ikea.com/ma/fr/images/products/vallentuna-sofa-bed-module-with-backrests-kelinge-rust__0938369_pe794076_s5.jpg?f=xxs 300w,
      https://www.ikea.com/ma/fr/images/products/vallentuna-sofa-bed-module-with-backrests-kelinge-rust__0938369_pe794076_s5.jpg?f=xxxs 160w,
      https://www.ikea.com/ma/fr/images/products/vallentuna-sofa-bed-module-with-backrests-kelinge-rust__0938369_pe794076_s5.jpg?f=u 80w
      "/>
                        </span>
                        <span class="range-revamp-aspect-ratio-image range-revamp-aspect-ratio-image--square range-revamp-product-compact__image-hover range-revamp-product-compact__image-hover--inactive">
                         <img alt="" class="range-revamp-aspect-ratio-image__image" data-src="https://www.ikea.com/ma/fr/images/products/vallentuna-sofa-bed-module-with-backrests-kelinge-rust__0938959_pe794357_s5.jpg?f=xxs" data-src-set="
      https://www.ikea.com/ma/fr/images/products/vallentuna-sofa-bed-module-with-backrests-kelinge-rust__0938959_pe794357_s5.jpg?f=m 600w,
      https://www.ikea.com/ma/fr/images/products/vallentuna-sofa-bed-module-with-backrests-kelinge-rust__0938959_pe794357_s5.jpg?f=xxs 300w,
      https://www.ikea.com/ma/fr/images/products/vallentuna-sofa-bed-module-with-backrests-kelinge-rust__0938959_pe794357_s5.jpg?f=xxxs 160w,
      https://www.ikea.com/ma/fr/images/products/vallentuna-sofa-bed-module-with-backrests-kelinge-rust__0938959_pe794357_s5.jpg?f=u 80w
      " loading="lazy" sizes="(max-width: 400px) 80px, (max-width: 1450px) 160px, 300px" src="data:image/gif;base64,R0lGODdhAQABAIAAAP///wAAACwAAAAAAQABAAACAkQBADs=" srcset=""/>
                        </span>
                       </div>
                      </a>
                      <div class="range-revamp-product-compact__bottom-wrapper">
                       <a class="range-revamp-product-compact__wrapper-link" href="https://www.ikea.com/ma/fr/p/vallentuna-module-convertible-avec-dossiers-kelinge-rouille-s79396442/">
                        <div class="range-revamp-compact-price-package">
                         <div class="range-revamp-compact-price-package__additional-info">
                          <div class="range-revamp-header-section">
                           <div class="range-revamp-header-section__title--small notranslate">
                            VALLENTUNA
                           </div>
                           <div class="range-revamp-header-section__description">
                            <span class="range-revamp-header-section__description-text">
                             Module convertible avec dossiers
                            </span>
                           </div>
                          </div>
                         </div>
                         <div class="range-revamp-compact-price-package__previous-price-wrapper">
                         </div>
                         <div class="range-revamp-compact-price-package__price-wrapper">
                          <span class="range-revamp-price">
                           <span class="range-revamp-price__integer">
                            8 390
                           </span>
                           <span class="range-revamp-price__currency-symbol range-revamp-price__currency-symbol--trailing range-revamp-price__currency-symbol--superscript">
                            DH
                           </span>
                          </span>
                         </div>
                         <span class="range-revamp-compact-price-package__variations-disclaimer" data-product-compact-gpr="">
                          Plus d'options
                         </span>
                        </div>
                       </a>
                      </div>
                     </div>
                    </div>
                   </div>
                   <div class="pub__carousel-slide ixrpjrm">
                    <div data-pub-hydrate-child="pub-carousel">
                    </div>
                   </div>
                   <div class="pub__carousel-slide ixrpjrm">
                    <div data-pub-hydrate-child="pub-carousel">
                     <div class="range-revamp-product-compact" data-cs-capture="" data-currency="MAD" data-price="3495" data-product-compact="" data-product-name="ASARUM" data-product-number="50284647" data-product-type="ART" data-ref-id="50284647">
                      <button aria-label="Ajouter à mes favoris" aria-pressed="false" class="range-revamp-toggle-button range-revamp-toggle-button--icon-only range-revamp-toggle-button--transparent range-revamp-product-compact__add-to-list-button">
                       <svg aria-hidden="true" class="range-revamp-svg-icon" focusable="false" viewbox="0 0 24 24">
                        <path clip-rule="evenodd" d="M12.336 5.52055C14.2336 3.62376 17.3096 3.62401 19.2069 5.52129C20.2067 6.52115 20.6796 7.85005 20.6259 9.15761C20.6151 12.2138 18.4184 14.8654 16.4892 16.6366C15.4926 17.5517 14.5004 18.2923 13.7593 18.8036C13.3879 19.0598 13.0771 19.2601 12.8574 19.3973C12.7475 19.466 12.6601 19.519 12.5992 19.5555C12.5687 19.5737 12.5448 19.5879 12.5279 19.5978L12.5079 19.6094L12.502 19.6129L12.5001 19.614C12.5001 19.614 12.4989 19.6147 11.9999 18.748C11.501 19.6147 11.5005 19.6144 11.5005 19.6144L11.4979 19.6129L11.4919 19.6094L11.472 19.5978C11.4551 19.5879 11.4312 19.5737 11.4007 19.5555C11.3397 19.519 11.2524 19.466 11.1425 19.3973C10.9227 19.2601 10.612 19.0598 10.2405 18.8036C9.49947 18.2923 8.50726 17.5517 7.51063 16.6366C5.58146 14.8654 3.38477 12.2139 3.37399 9.15765C3.32024 7.85008 3.79314 6.52117 4.79301 5.52129C6.69054 3.62376 9.76704 3.62376 11.6646 5.52129L11.9993 5.856L12.3353 5.52129L12.336 5.52055ZM11.9999 18.748L11.5005 19.6144L11.9999 19.9019L12.4989 19.6147L11.9999 18.748ZM11.9999 17.573C12.1727 17.462 12.384 17.3226 12.6236 17.1573C13.3125 16.6821 14.2267 15.9988 15.1366 15.1634C17.0157 13.4381 18.6259 11.2919 18.6259 9.13506V9.11213L18.627 9.08922C18.6626 8.31221 18.3844 7.52727 17.7926 6.9355C16.6762 5.81903 14.866 5.81902 13.7495 6.9355L13.7481 6.93689L11.9965 8.68166L10.2504 6.9355C9.13387 5.81903 7.3237 5.81903 6.20722 6.9355C5.61546 7.52727 5.33724 8.31221 5.3729 9.08922L5.37395 9.11213V9.13507C5.37395 11.2919 6.98418 13.4381 8.86325 15.1634C9.77312 15.9988 10.6874 16.6821 11.3762 17.1573C11.6159 17.3226 11.8271 17.462 11.9999 17.573Z" fill-rule="evenodd">
                        </path>
                       </svg>
                      </button>
                      <a aria-label="ASARUM - Convertible 3 places" href="https://www.ikea.com/ma/fr/p/asarum-convertible-3-places-gris-50284647/">
                       <div class="range-revamp-product-compact__image-wrapper">
                        <span class="range-revamp-aspect-ratio-image range-revamp-aspect-ratio-image--square">
                         <img alt="ASARUM Convertible 3 places, gris" class="range-revamp-aspect-ratio-image__image" loading="lazy" sizes="(max-width: 400px) 80px, (max-width: 1450px) 160px, 300px" src="https://www.ikea.com/ma/fr/images/products/asarum-three-seat-sofa-bed-grey__1028492_pe835377_s5.jpg?f=xxs" srcset="
      https://www.ikea.com/ma/fr/images/products/asarum-three-seat-sofa-bed-grey__1028492_pe835377_s5.jpg?f=m 600w,
      https://www.ikea.com/ma/fr/images/products/asarum-three-seat-sofa-bed-grey__1028492_pe835377_s5.jpg?f=xxs 300w,
      https://www.ikea.com/ma/fr/images/products/asarum-three-seat-sofa-bed-grey__1028492_pe835377_s5.jpg?f=xxxs 160w,
      https://www.ikea.com/ma/fr/images/products/asarum-three-seat-sofa-bed-grey__1028492_pe835377_s5.jpg?f=u 80w
      "/>
                        </span>
                        <span class="range-revamp-aspect-ratio-image range-revamp-aspect-ratio-image--square range-revamp-product-compact__image-hover range-revamp-product-compact__image-hover--inactive">
                         <img alt="" class="range-revamp-aspect-ratio-image__image" data-src="https://www.ikea.com/ma/fr/images/products/asarum-three-seat-sofa-bed-grey__1028494_pe835379_s5.jpg?f=xxs" data-src-set="
      https://www.ikea.com/ma/fr/images/products/asarum-three-seat-sofa-bed-grey__1028494_pe835379_s5.jpg?f=m 600w,
      https://www.ikea.com/ma/fr/images/products/asarum-three-seat-sofa-bed-grey__1028494_pe835379_s5.jpg?f=xxs 300w,
      https://www.ikea.com/ma/fr/images/products/asarum-three-seat-sofa-bed-grey__1028494_pe835379_s5.jpg?f=xxxs 160w,
      https://www.ikea.com/ma/fr/images/products/asarum-three-seat-sofa-bed-grey__1028494_pe835379_s5.jpg?f=u 80w
      " loading="lazy" sizes="(max-width: 400px) 80px, (max-width: 1450px) 160px, 300px" src="data:image/gif;base64,R0lGODdhAQABAIAAAP///wAAACwAAAAAAQABAAACAkQBADs=" srcset=""/>
                        </span>
                       </div>
                      </a>
                      <div class="range-revamp-product-compact__bottom-wrapper">
                       <a class="range-revamp-product-compact__wrapper-link" href="https://www.ikea.com/ma/fr/p/asarum-convertible-3-places-gris-50284647/">
                        <div class="range-revamp-compact-price-package">
                         <div class="range-revamp-compact-price-package__additional-info">
                          <div class="range-revamp-header-section">
                           <div class="range-revamp-header-section__title--small notranslate">
                            ASARUM
                           </div>
                           <div class="range-revamp-header-section__description">
                            <span class="range-revamp-header-section__description-text">
                             Convertible 3 places
                            </span>
                           </div>
                          </div>
                         </div>
                         <div class="range-revamp-compact-price-package__previous-price-wrapper">
                         </div>
                         <div class="range-revamp-compact-price-package__price-wrapper">
                          <span class="range-revamp-price">
                           <span class="range-revamp-price__integer">
                            3 495
                           </span>
                           <span class="range-revamp-price__currency-symbol range-revamp-price__currency-symbol--trailing range-revamp-price__currency-symbol--superscript">
                            DH
                           </span>
                          </span>
                         </div>
                         <span class="range-revamp-compact-price-package__variations-disclaimer" data-product-compact-gpr="">
                          Plus d'options
                         </span>
                        </div>
                       </a>
                      </div>
                     </div>
                    </div>
                   </div>
                  </div>
                 </div>
                </div>
                <button aria-controls="pub__carousel__3b31afb0-202a-11ec-96f0-d900bf02a083" aria-label="See next items" class="pub__btn pub__btn--small pub__btn--icon-primary pub__carousel__button pub__carousel__button--right" id="pub__-carousel__3b31afb0-202a-11ec-96f0-d900bf02a083-next-btn" type="button">
                 <span class="pub__btn__inner">
                  <svg aria-hidden="true" class="pub__svg-icon pub__btn__icon" focusable="false" viewbox="0 0 24 24">
                   <path clip-rule="evenodd" d="m16.415 12.0011-8.0012 8.0007-1.4141-1.4143 6.587-6.5866-6.586-6.5868L8.415 4l8 8.0011z" fill-rule="evenodd">
                   </path>
                  </svg>
                 </span>
                </button>
               </div>
               <div class="pub__scroll-indicator" tabindex="0">
               </div>
               <a id="pub__-carousel__3b31afb0-202a-11ec-96f0-d900bf02a083-skip-btn">
               </a>
              </div>
             </div>
            </div>
            <a class="pub__teaser__bottom-button pub__chunky-header pub__chunky-header--small" href="https://www.ikea.com/ma/fr/cat/convertibles-10663/">
             <span class="pub__chunky-header__title-wrapper">
              <span class="pub__chunky-header__title">
               Voir tous nos convertibles
              </span>
             </span>
             <svg aria-hidden="true" class="pub__svg-icon pub__chunky-header__icon" focusable="false" viewbox="0 0 24 24">
              <path clip-rule="evenodd" d="m15.5996 12.0007-5.785 5.7857-1.4143-1.4141 4.3711-4.3716L8.4003 7.629l1.4143-1.4142 5.785 5.7859z" fill-rule="evenodd">
              </path>
             </svg>
            </a>
           </div>
          </div>
         </div>
        </section>
        <section class="gd8xc1c v19w64p3 v18by0fb">
         <div id="99e268b0-202a-11ec-96f0-d900bf02a083">
          <div class="stuc9r1">
           <div class="c3m3un1" data-pub-id="99e63940-202a-11ec-96f0-d900bf02a083" data-pub-itemindex="0" data-pub-type="assurances-item">
            <svg aria-hidden="true" class="pub__svg-icon c21nsg2" focusable="false" viewbox="0 0 24 24">
             <path clip-rule="evenodd" d="M14 6H5v3h9V6zM3 4v7h3.983l-2.3093 4H3v6h11v-6h-3.5445l2.3094-4H16V9h2V8h3V6h-3V5h-2V4H3zm7.4555 7-2.3094 4H6.983l2.3094-4h1.163zM5 17h7v2H5v-2z" fill-rule="evenodd">
             </path>
            </svg>
            <h3 class="c20sqpi">
             Montage
            </h3>
            <p class="cqhfxlu">
             Un service pro – à domicile ou au travail
            </p>
            <a class="cqndvw5 pub__link" href="https://www.ikea.com/ma/fr/customer-service/services/assembly/">
             En savoir plus
            </a>
           </div>
           <div class="c3m3un1" data-pub-id="9b7df040-202a-11ec-96f0-d900bf02a083" data-pub-itemindex="1" data-pub-type="assurances-item">
            <svg aria-hidden="true" class="pub__svg-icon c21nsg2" focusable="false" viewbox="0 0 24 24">
             <path clip-rule="evenodd" d="M21 4H1v16h15V10H6v8H3V6h16v7.1707c-1.1652.4118-2 1.5231-2 2.8293v3c0 1.6569 1.3431 3 3 3s3-1.3431 3-3v-3c0-1.3062-.8348-2.4175-2-2.8293V4zM8 18h2v-6H8v6zm6 0h-2v-6h2v6zm5-2c0-.5523.4477-1 1-1s1 .4477 1 1v3c0 .5523-.4477 1-1 1s-1-.4477-1-1v-3z" fill-rule="evenodd">
             </path>
            </svg>
            <h3 class="c20sqpi">
             Click &amp; Collect
            </h3>
            <p class="cqhfxlu">
             Venez chercher votre commande
            </p>
            <a class="cqndvw5 pub__link" href="https://www.ikea.com/ma/fr/customer-service/services/click-collect/">
             En savoir plus
            </a>
           </div>
           <div class="c3m3un1" data-pub-id="db5efe40-21d1-11ec-bb83-d131072d8dee" data-pub-itemindex="2" data-pub-type="assurances-item">
            <svg aria-hidden="true" class="pub__svg-icon c21nsg2" focusable="false" viewbox="0 0 24 24">
             <path clip-rule="evenodd" d="M5 5C3.3432 5 2 6.3431 2 8v8c0 1.6569 1.3432 3 3 3h14c1.6569 0 3-1.3431 3-3V8c0-1.6569-1.3431-3-3-3H5zM4 8c0-.5523.4477-1 1-1h14c.5523 0 1 .4477 1 1v1H4V8zm0 4v4c0 .5523.4477 1 1 1h14c.5523 0 1-.4477 1-1v-4H4z" fill-rule="evenodd">
             </path>
            </svg>
            <h3 class="c20sqpi">
             Modes de paiement
            </h3>
            <p class="cqhfxlu">
             Comment payer, en magasin et en ligne
            </p>
            <a class="cqndvw5 pub__link" href="">
             En savoir plus
            </a>
           </div>
          </div>
         </div>
        </section>
        <section class="gd8xc1c v19w64p3 v18by0fb">
         <div id="9f3727b0-202a-11ec-96f0-d900bf02a083">
          <div class="o40z9vt">
           <div class="gd8xc1c v11tpn0s v18by0fb" data-pub-id="9f3727b0-202a-11ec-96f0-d900bf02a083" data-pub-type="visual-pill-slider">
            <h2 class="c1m1sl8e pub__h2 s1gshh7t">
             Offrez-vous des produits adaptés à des modes de vie plus écologiques
            </h2>
            <div data-pub-hydrate="pub-carousel" data-seed='{"id":"9f3727b0-202a-11ec-96f0-d900bf02a083","prefix":"pub__","itemClass":"i1q4hu9o","rtl":false}' style="height:100%">
             <div class="pub__carousel" tabindex="-1">
              <a class="btn btn--primary-inverse pub__carousel__skip-button" href="#pub__-carousel__9f3727b0-202a-11ec-96f0-d900bf02a083-skip-btn" role="button">
               <span class="btn__inner">
                Skip listing
               </span>
              </a>
              <div class="pub__carousel__wrapper">
               <button aria-controls="pub__carousel__9f3727b0-202a-11ec-96f0-d900bf02a083" aria-label="See previous items" class="pub__btn pub__btn--small pub__btn--icon-primary pub__carousel__button" id="pub__-carousel__9f3727b0-202a-11ec-96f0-d900bf02a083-prev-btn" type="button">
                <span class="pub__btn__inner">
                 <svg aria-hidden="true" class="pub__svg-icon pub__btn__icon" focusable="false" viewbox="0 0 24 24">
                  <path clip-rule="evenodd" d="m7 12.0009 8.0012-8.0007 1.4142 1.4142-6.587 6.5866 6.5859 6.5868L15 20.002l-8-8.0011z" fill-rule="evenodd">
                  </path>
                 </svg>
                </span>
               </button>
               <div class="pub__carousel__content pub__carousel__content--snap-slide">
                <div class="pub__carousel__body-wrapper">
                 <div class="pub__carousel__body" id="pub__carousel__9f3727b0-202a-11ec-96f0-d900bf02a083">
                  <div class="pub__carousel-slide i1q4hu9o">
                   <div class="" data-pub-hydrate-child="pub-carousel" role="list" style="height:100%;width:100%">
                    <div class="c1p6qo7v f7zhins r5llg8g" data-pub-id="9f3a34f0-202a-11ec-96f0-d900bf02a083" data-pub-itemindex="0" data-pub-type="visual-pill-slider-item" role="listitem" tabindex="-1">
                     <a class="shvht8j" href="https://www.ikea.com/ma/fr/product-guides/sustainable-products/saving-water/">
                      <span class="pub__aspect-ratio-image pub__aspect-ratio-image--portrait">
                       <img alt="Une main règle le débit d’un robinet de cuisine GLYPEN en acier inoxydable. Une brosse TÅRTSMET pour la vaisselle est posée à proximité." aria-labelledby="9f3a34f0-202a-11ec-96f0-d900bf02a083-button" class="pub__aspect-ratio-image__image" loading="lazy" sizes="272px" src="https://www.ikea.com/images/une-main-regle-le-debit-dun-robinet-de-cuisine-glypen-en-aci-2d046b82e457762470d3842384f874e7.jpg?f=s" srcset="https://www.ikea.com/images/une-main-regle-le-debit-dun-robinet-de-cuisine-glypen-en-aci-2d046b82e457762470d3842384f874e7.jpg?f=sg 1600w,
  https://www.ikea.com/images/une-main-regle-le-debit-dun-robinet-de-cuisine-glypen-en-aci-2d046b82e457762470d3842384f874e7.jpg?f=xxxl 1400w,
  https://www.ikea.com/images/une-main-regle-le-debit-dun-robinet-de-cuisine-glypen-en-aci-2d046b82e457762470d3842384f874e7.jpg?f=xxl 950w,
  https://www.ikea.com/images/une-main-regle-le-debit-dun-robinet-de-cuisine-glypen-en-aci-2d046b82e457762470d3842384f874e7.jpg?f=xl 800w,
  https://www.ikea.com/images/une-main-regle-le-debit-dun-robinet-de-cuisine-glypen-en-aci-2d046b82e457762470d3842384f874e7.jpg?f=l 750w,
  https://www.ikea.com/images/une-main-regle-le-debit-dun-robinet-de-cuisine-glypen-en-aci-2d046b82e457762470d3842384f874e7.jpg?f=m 600w,
  https://www.ikea.com/images/une-main-regle-le-debit-dun-robinet-de-cuisine-glypen-en-aci-2d046b82e457762470d3842384f874e7.jpg?f=s 500w,
  https://www.ikea.com/images/une-main-regle-le-debit-dun-robinet-de-cuisine-glypen-en-aci-2d046b82e457762470d3842384f874e7.jpg?f=xs 400w,
  https://www.ikea.com/images/une-main-regle-le-debit-dun-robinet-de-cuisine-glypen-en-aci-2d046b82e457762470d3842384f874e7.jpg?f=xxs 300w,
  https://www.ikea.com/images/une-main-regle-le-debit-dun-robinet-de-cuisine-glypen-en-aci-2d046b82e457762470d3842384f874e7.jpg?f=xxxs 240w"/>
                      </span>
                     </a>
                     <div class="bh9ulou">
                      <a aria-hidden="true" class="pub__btn pub__btn--small pub__btn--primary-inverse" href="https://www.ikea.com/ma/fr/product-guides/sustainable-products/saving-water/" id="9f3a34f0-202a-11ec-96f0-d900bf02a083-button" role="button" tabindex="-1">
                       <span class="pub__btn__inner">
                        <span class="pub__btn__label">
                         Économies d’eau
                        </span>
                       </span>
                      </a>
                     </div>
                    </div>
                   </div>
                  </div>
                  <div class="pub__carousel-slide i1q4hu9o">
                   <div class="" data-pub-hydrate-child="pub-carousel" role="list" style="height:100%;width:100%">
                    <div class="c1p6qo7v f7zhins r5llg8g" data-pub-id="b11d85a0-202a-11ec-96f0-d900bf02a083" data-pub-itemindex="1" data-pub-type="visual-pill-slider-item" role="listitem" tabindex="-1">
                     <a class="shvht8j" href="https://www.ikea.com/ma/fr/product-guides/sustainable-products/saving-energy/">
                      <span class="pub__aspect-ratio-image pub__aspect-ratio-image--portrait">
                       <img alt="Une main actionne l’interrupteur d’une lampe de table blanche posée sur une table bleu clair." aria-labelledby="b11d85a0-202a-11ec-96f0-d900bf02a083-button" class="pub__aspect-ratio-image__image" loading="lazy" sizes="272px" src="https://www.ikea.com/images/une-main-actionne-linterrupteur-dune-lampe-de-table-blanche--011d35f852f843621bc19283d76bb6ee.jpg?f=s" srcset="https://www.ikea.com/images/une-main-actionne-linterrupteur-dune-lampe-de-table-blanche--011d35f852f843621bc19283d76bb6ee.jpg?f=sg 1600w,
  https://www.ikea.com/images/une-main-actionne-linterrupteur-dune-lampe-de-table-blanche--011d35f852f843621bc19283d76bb6ee.jpg?f=xxxl 1400w,
  https://www.ikea.com/images/une-main-actionne-linterrupteur-dune-lampe-de-table-blanche--011d35f852f843621bc19283d76bb6ee.jpg?f=xxl 950w,
  https://www.ikea.com/images/une-main-actionne-linterrupteur-dune-lampe-de-table-blanche--011d35f852f843621bc19283d76bb6ee.jpg?f=xl 800w,
  https://www.ikea.com/images/une-main-actionne-linterrupteur-dune-lampe-de-table-blanche--011d35f852f843621bc19283d76bb6ee.jpg?f=l 750w,
  https://www.ikea.com/images/une-main-actionne-linterrupteur-dune-lampe-de-table-blanche--011d35f852f843621bc19283d76bb6ee.jpg?f=m 600w,
  https://www.ikea.com/images/une-main-actionne-linterrupteur-dune-lampe-de-table-blanche--011d35f852f843621bc19283d76bb6ee.jpg?f=s 500w,
  https://www.ikea.com/images/une-main-actionne-linterrupteur-dune-lampe-de-table-blanche--011d35f852f843621bc19283d76bb6ee.jpg?f=xs 400w,
  https://www.ikea.com/images/une-main-actionne-linterrupteur-dune-lampe-de-table-blanche--011d35f852f843621bc19283d76bb6ee.jpg?f=xxs 300w,
  https://www.ikea.com/images/une-main-actionne-linterrupteur-dune-lampe-de-table-blanche--011d35f852f843621bc19283d76bb6ee.jpg?f=xxxs 240w"/>
                      </span>
                     </a>
                     <div class="bh9ulou">
                      <a aria-hidden="true" class="pub__btn pub__btn--small pub__btn--primary-inverse" href="https://www.ikea.com/ma/fr/product-guides/sustainable-products/saving-energy/" id="b11d85a0-202a-11ec-96f0-d900bf02a083-button" role="button" tabindex="-1">
                       <span class="pub__btn__inner">
                        <span class="pub__btn__label">
                         Économies d’énergie
                        </span>
                       </span>
                      </a>
                     </div>
                    </div>
                   </div>
                  </div>
                  <div class="pub__carousel-slide i1q4hu9o">
                   <div class="" data-pub-hydrate-child="pub-carousel" role="list" style="height:100%;width:100%">
                    <div class="c1p6qo7v f7zhins r5llg8g" data-pub-id="bd94e5d0-202a-11ec-96f0-d900bf02a083" data-pub-itemindex="2" data-pub-type="visual-pill-slider-item" role="listitem" tabindex="-1">
                     <a class="shvht8j" href="https://www.ikea.com/ma/fr/product-guides/sustainable-products/healthy-homes/">
                      <span class="pub__aspect-ratio-image pub__aspect-ratio-image--portrait">
                       <img alt="Femme aux cheveux bruns vêtue d’une chemise blanche, endormie sous une couverture blanche. Sa tête repose sur un oreiller ergonomique ROSENSKÄRM." aria-labelledby="bd94e5d0-202a-11ec-96f0-d900bf02a083-button" class="pub__aspect-ratio-image__image" loading="lazy" sizes="272px" src="https://www.ikea.com/images/femme-aux-cheveux-bruns-vetue-dune-chemise-blanche-endormie--ad2702f8ff63778f63856aaeec679a1e.jpg?f=s" srcset="https://www.ikea.com/images/femme-aux-cheveux-bruns-vetue-dune-chemise-blanche-endormie--ad2702f8ff63778f63856aaeec679a1e.jpg?f=sg 1600w,
  https://www.ikea.com/images/femme-aux-cheveux-bruns-vetue-dune-chemise-blanche-endormie--ad2702f8ff63778f63856aaeec679a1e.jpg?f=xxxl 1400w,
  https://www.ikea.com/images/femme-aux-cheveux-bruns-vetue-dune-chemise-blanche-endormie--ad2702f8ff63778f63856aaeec679a1e.jpg?f=xxl 950w,
  https://www.ikea.com/images/femme-aux-cheveux-bruns-vetue-dune-chemise-blanche-endormie--ad2702f8ff63778f63856aaeec679a1e.jpg?f=xl 800w,
  https://www.ikea.com/images/femme-aux-cheveux-bruns-vetue-dune-chemise-blanche-endormie--ad2702f8ff63778f63856aaeec679a1e.jpg?f=l 750w,
  https://www.ikea.com/images/femme-aux-cheveux-bruns-vetue-dune-chemise-blanche-endormie--ad2702f8ff63778f63856aaeec679a1e.jpg?f=m 600w,
  https://www.ikea.com/images/femme-aux-cheveux-bruns-vetue-dune-chemise-blanche-endormie--ad2702f8ff63778f63856aaeec679a1e.jpg?f=s 500w,
  https://www.ikea.com/images/femme-aux-cheveux-bruns-vetue-dune-chemise-blanche-endormie--ad2702f8ff63778f63856aaeec679a1e.jpg?f=xs 400w,
  https://www.ikea.com/images/femme-aux-cheveux-bruns-vetue-dune-chemise-blanche-endormie--ad2702f8ff63778f63856aaeec679a1e.jpg?f=xxs 300w,
  https://www.ikea.com/images/femme-aux-cheveux-bruns-vetue-dune-chemise-blanche-endormie--ad2702f8ff63778f63856aaeec679a1e.jpg?f=xxxs 240w"/>
                      </span>
                     </a>
                     <div class="bh9ulou">
                      <a aria-hidden="true" class="pub__btn pub__btn--small pub__btn--primary-inverse" href="https://www.ikea.com/ma/fr/product-guides/sustainable-products/healthy-homes/" id="bd94e5d0-202a-11ec-96f0-d900bf02a083-button" role="button" tabindex="-1">
                       <span class="pub__btn__inner">
                        <span class="pub__btn__label">
                         Un intérieur plus sain
                        </span>
                       </span>
                      </a>
                     </div>
                    </div>
                   </div>
                  </div>
                  <div class="pub__carousel-slide i1q4hu9o">
                   <div class="" data-pub-hydrate-child="pub-carousel" role="list" style="height:100%;width:100%">
                    <div class="c1p6qo7v f7zhins r5llg8g" data-pub-id="c8eea100-202a-11ec-96f0-d900bf02a083" data-pub-itemindex="3" data-pub-type="visual-pill-slider-item" role="listitem" tabindex="-1">
                     <a class="shvht8j" href="https://www.ikea.com/ma/fr/product-guides/sustainable-products/reducing-waste/">
                      <span class="pub__aspect-ratio-image pub__aspect-ratio-image--portrait">
                       <img alt="Trois bacs SORTERA en blanc dans une pièce carrelée de blanc. L’un des bacs est rempli de papier kraft." aria-labelledby="c8eea100-202a-11ec-96f0-d900bf02a083-button" class="pub__aspect-ratio-image__image" loading="lazy" sizes="272px" src="https://www.ikea.com/images/trois-bacs-sortera-en-blanc-dans-une-piece-carrelee-de-blanc-64203f2f7c488633537a71dcef6fb386.jpg?f=s" srcset="https://www.ikea.com/images/trois-bacs-sortera-en-blanc-dans-une-piece-carrelee-de-blanc-64203f2f7c488633537a71dcef6fb386.jpg?f=sg 1600w,
  https://www.ikea.com/images/trois-bacs-sortera-en-blanc-dans-une-piece-carrelee-de-blanc-64203f2f7c488633537a71dcef6fb386.jpg?f=xxxl 1400w,
  https://www.ikea.com/images/trois-bacs-sortera-en-blanc-dans-une-piece-carrelee-de-blanc-64203f2f7c488633537a71dcef6fb386.jpg?f=xxl 950w,
  https://www.ikea.com/images/trois-bacs-sortera-en-blanc-dans-une-piece-carrelee-de-blanc-64203f2f7c488633537a71dcef6fb386.jpg?f=xl 800w,
  https://www.ikea.com/images/trois-bacs-sortera-en-blanc-dans-une-piece-carrelee-de-blanc-64203f2f7c488633537a71dcef6fb386.jpg?f=l 750w,
  https://www.ikea.com/images/trois-bacs-sortera-en-blanc-dans-une-piece-carrelee-de-blanc-64203f2f7c488633537a71dcef6fb386.jpg?f=m 600w,
  https://www.ikea.com/images/trois-bacs-sortera-en-blanc-dans-une-piece-carrelee-de-blanc-64203f2f7c488633537a71dcef6fb386.jpg?f=s 500w,
  https://www.ikea.com/images/trois-bacs-sortera-en-blanc-dans-une-piece-carrelee-de-blanc-64203f2f7c488633537a71dcef6fb386.jpg?f=xs 400w,
  https://www.ikea.com/images/trois-bacs-sortera-en-blanc-dans-une-piece-carrelee-de-blanc-64203f2f7c488633537a71dcef6fb386.jpg?f=xxs 300w,
  https://www.ikea.com/images/trois-bacs-sortera-en-blanc-dans-une-piece-carrelee-de-blanc-64203f2f7c488633537a71dcef6fb386.jpg?f=xxxs 240w"/>
                      </span>
                     </a>
                     <div class="bh9ulou">
                      <a aria-hidden="true" class="pub__btn pub__btn--small pub__btn--primary-inverse" href="https://www.ikea.com/ma/fr/product-guides/sustainable-products/reducing-waste/" id="c8eea100-202a-11ec-96f0-d900bf02a083-button" role="button" tabindex="-1">
                       <span class="pub__btn__inner">
                        <span class="pub__btn__label">
                         Réduction des déchets
                        </span>
                       </span>
                      </a>
                     </div>
                    </div>
                   </div>
                  </div>
                  <div class="pub__carousel-slide i1q4hu9o">
                   <div class="" data-pub-hydrate-child="pub-carousel" role="list" style="height:100%;width:100%">
                    <div class="c1p6qo7v f7zhins r5llg8g" data-pub-id="d4443d80-202a-11ec-96f0-d900bf02a083" data-pub-itemindex="4" data-pub-type="visual-pill-slider-item" role="listitem" tabindex="-1">
                     <a class="shvht8j" href="https://www.ikea.com/ma/fr/product-guides/sustainable-products/sustainable-furniture/">
                      <span class="pub__aspect-ratio-image pub__aspect-ratio-image--portrait">
                       <img alt="Chaise IVAR vert clair posée sur de vieux journaux dans une pièce vide au plancher clair et aux murs rose pâle." aria-labelledby="d4443d80-202a-11ec-96f0-d900bf02a083-button" class="pub__aspect-ratio-image__image" loading="lazy" sizes="272px" src="https://www.ikea.com/images/chaise-ivar-vert-clair-posee-sur-de-vieux-journaux-dans-une--5bdb5524e50909d5914974fdcda2a5b6.jpg?f=s" srcset="https://www.ikea.com/images/chaise-ivar-vert-clair-posee-sur-de-vieux-journaux-dans-une--5bdb5524e50909d5914974fdcda2a5b6.jpg?f=sg 1600w,
  https://www.ikea.com/images/chaise-ivar-vert-clair-posee-sur-de-vieux-journaux-dans-une--5bdb5524e50909d5914974fdcda2a5b6.jpg?f=xxxl 1400w,
  https://www.ikea.com/images/chaise-ivar-vert-clair-posee-sur-de-vieux-journaux-dans-une--5bdb5524e50909d5914974fdcda2a5b6.jpg?f=xxl 950w,
  https://www.ikea.com/images/chaise-ivar-vert-clair-posee-sur-de-vieux-journaux-dans-une--5bdb5524e50909d5914974fdcda2a5b6.jpg?f=xl 800w,
  https://www.ikea.com/images/chaise-ivar-vert-clair-posee-sur-de-vieux-journaux-dans-une--5bdb5524e50909d5914974fdcda2a5b6.jpg?f=l 750w,
  https://www.ikea.com/images/chaise-ivar-vert-clair-posee-sur-de-vieux-journaux-dans-une--5bdb5524e50909d5914974fdcda2a5b6.jpg?f=m 600w,
  https://www.ikea.com/images/chaise-ivar-vert-clair-posee-sur-de-vieux-journaux-dans-une--5bdb5524e50909d5914974fdcda2a5b6.jpg?f=s 500w,
  https://www.ikea.com/images/chaise-ivar-vert-clair-posee-sur-de-vieux-journaux-dans-une--5bdb5524e50909d5914974fdcda2a5b6.jpg?f=xs 400w,
  https://www.ikea.com/images/chaise-ivar-vert-clair-posee-sur-de-vieux-journaux-dans-une--5bdb5524e50909d5914974fdcda2a5b6.jpg?f=xxs 300w,
  https://www.ikea.com/images/chaise-ivar-vert-clair-posee-sur-de-vieux-journaux-dans-une--5bdb5524e50909d5914974fdcda2a5b6.jpg?f=xxxs 240w"/>
                      </span>
                     </a>
                     <div class="bh9ulou">
                      <a aria-hidden="true" class="pub__btn pub__btn--small pub__btn--primary-inverse" href="https://www.ikea.com/ma/fr/product-guides/sustainable-products/sustainable-furniture/" id="d4443d80-202a-11ec-96f0-d900bf02a083-button" role="button" tabindex="-1">
                       <span class="pub__btn__inner">
                        <span class="pub__btn__label">
                         Un mobilier plus écologique
                        </span>
                       </span>
                      </a>
                     </div>
                    </div>
                   </div>
                  </div>
                  <div class="pub__carousel-slide i1q4hu9o">
                   <div class="" data-pub-hydrate-child="pub-carousel" role="list" style="height:100%;width:100%">
                    <div class="c1p6qo7v f7zhins r5llg8g" data-pub-id="e0beaaf0-202a-11ec-96f0-d900bf02a083" data-pub-itemindex="5" data-pub-type="visual-pill-slider-item" role="listitem" tabindex="-1">
                     <a class="shvht8j" href="https://www.ikea.com/ma/fr/product-guides/sustainable-products/sustainable-materials/">
                      <span class="pub__aspect-ratio-image pub__aspect-ratio-image--portrait">
                       <img alt="Couverture blanche et trois bols blancs sur un repose-pieds GAMLEHULT dans lequel sont rangés des livres." aria-labelledby="e0beaaf0-202a-11ec-96f0-d900bf02a083-button" class="pub__aspect-ratio-image__image" loading="lazy" sizes="272px" src="https://www.ikea.com/images/couverture-blanche-et-trois-bols-blancs-sur-un-repose-pieds--c2af9914f5e0328f9c047ea5bd037bce.jpg?f=s" srcset="https://www.ikea.com/images/couverture-blanche-et-trois-bols-blancs-sur-un-repose-pieds--c2af9914f5e0328f9c047ea5bd037bce.jpg?f=sg 1600w,
  https://www.ikea.com/images/couverture-blanche-et-trois-bols-blancs-sur-un-repose-pieds--c2af9914f5e0328f9c047ea5bd037bce.jpg?f=xxxl 1400w,
  https://www.ikea.com/images/couverture-blanche-et-trois-bols-blancs-sur-un-repose-pieds--c2af9914f5e0328f9c047ea5bd037bce.jpg?f=xxl 950w,
  https://www.ikea.com/images/couverture-blanche-et-trois-bols-blancs-sur-un-repose-pieds--c2af9914f5e0328f9c047ea5bd037bce.jpg?f=xl 800w,
  https://www.ikea.com/images/couverture-blanche-et-trois-bols-blancs-sur-un-repose-pieds--c2af9914f5e0328f9c047ea5bd037bce.jpg?f=l 750w,
  https://www.ikea.com/images/couverture-blanche-et-trois-bols-blancs-sur-un-repose-pieds--c2af9914f5e0328f9c047ea5bd037bce.jpg?f=m 600w,
  https://www.ikea.com/images/couverture-blanche-et-trois-bols-blancs-sur-un-repose-pieds--c2af9914f5e0328f9c047ea5bd037bce.jpg?f=s 500w,
  https://www.ikea.com/images/couverture-blanche-et-trois-bols-blancs-sur-un-repose-pieds--c2af9914f5e0328f9c047ea5bd037bce.jpg?f=xs 400w,
  https://www.ikea.com/images/couverture-blanche-et-trois-bols-blancs-sur-un-repose-pieds--c2af9914f5e0328f9c047ea5bd037bce.jpg?f=xxs 300w,
  https://www.ikea.com/images/couverture-blanche-et-trois-bols-blancs-sur-un-repose-pieds--c2af9914f5e0328f9c047ea5bd037bce.jpg?f=xxxs 240w"/>
                      </span>
                     </a>
                     <div class="bh9ulou">
                      <a aria-hidden="true" class="pub__btn pub__btn--small pub__btn--primary-inverse" href="https://www.ikea.com/ma/fr/product-guides/sustainable-products/sustainable-materials/" id="e0beaaf0-202a-11ec-96f0-d900bf02a083-button" role="button" tabindex="-1">
                       <span class="pub__btn__inner">
                        <span class="pub__btn__label">
                         Des matériaux plus écologiques
                        </span>
                       </span>
                      </a>
                     </div>
                    </div>
                   </div>
                  </div>
                  <div class="pub__carousel-slide i1q4hu9o">
                   <div class="" data-pub-hydrate-child="pub-carousel" role="list" style="height:100%;width:100%">
                    <div class="c1p6qo7v f7zhins r5llg8g" data-pub-id="f1ccd150-202a-11ec-96f0-d900bf02a083" data-pub-itemindex="6" data-pub-type="visual-pill-slider-item" role="listitem" tabindex="-1">
                     <a class="shvht8j" href="https://www.ikea.com/ma/fr/product-guides/sustainable-products/sustainable-food/">
                      <span class="pub__aspect-ratio-image pub__aspect-ratio-image--portrait">
                       <img alt="Une main assaisonne des boulettes végétales disposées dans une poêle à frire IKEA 365+." aria-labelledby="f1ccd150-202a-11ec-96f0-d900bf02a083-button" class="pub__aspect-ratio-image__image" loading="lazy" sizes="272px" src="https://www.ikea.com/images/une-main-assaisonne-des-boulettes-vegetales-disposees-dans-u-938af068518a412d136aa103baa2683e.jpg?f=s" srcset="https://www.ikea.com/images/une-main-assaisonne-des-boulettes-vegetales-disposees-dans-u-938af068518a412d136aa103baa2683e.jpg?f=sg 1600w,
  https://www.ikea.com/images/une-main-assaisonne-des-boulettes-vegetales-disposees-dans-u-938af068518a412d136aa103baa2683e.jpg?f=xxxl 1400w,
  https://www.ikea.com/images/une-main-assaisonne-des-boulettes-vegetales-disposees-dans-u-938af068518a412d136aa103baa2683e.jpg?f=xxl 950w,
  https://www.ikea.com/images/une-main-assaisonne-des-boulettes-vegetales-disposees-dans-u-938af068518a412d136aa103baa2683e.jpg?f=xl 800w,
  https://www.ikea.com/images/une-main-assaisonne-des-boulettes-vegetales-disposees-dans-u-938af068518a412d136aa103baa2683e.jpg?f=l 750w,
  https://www.ikea.com/images/une-main-assaisonne-des-boulettes-vegetales-disposees-dans-u-938af068518a412d136aa103baa2683e.jpg?f=m 600w,
  https://www.ikea.com/images/une-main-assaisonne-des-boulettes-vegetales-disposees-dans-u-938af068518a412d136aa103baa2683e.jpg?f=s 500w,
  https://www.ikea.com/images/une-main-assaisonne-des-boulettes-vegetales-disposees-dans-u-938af068518a412d136aa103baa2683e.jpg?f=xs 400w,
  https://www.ikea.com/images/une-main-assaisonne-des-boulettes-vegetales-disposees-dans-u-938af068518a412d136aa103baa2683e.jpg?f=xxs 300w,
  https://www.ikea.com/images/une-main-assaisonne-des-boulettes-vegetales-disposees-dans-u-938af068518a412d136aa103baa2683e.jpg?f=xxxs 240w"/>
                      </span>
                     </a>
                     <div class="bh9ulou">
                      <a aria-hidden="true" class="pub__btn pub__btn--small pub__btn--primary-inverse" href="https://www.ikea.com/ma/fr/product-guides/sustainable-products/sustainable-food/" id="f1ccd150-202a-11ec-96f0-d900bf02a083-button" role="button" tabindex="-1">
                       <span class="pub__btn__inner">
                        <span class="pub__btn__label">
                         Des aliments plus écologiques
                        </span>
                       </span>
                      </a>
                     </div>
                    </div>
                   </div>
                  </div>
                 </div>
                </div>
               </div>
               <button aria-controls="pub__carousel__9f3727b0-202a-11ec-96f0-d900bf02a083" aria-label="See next items" class="pub__btn pub__btn--small pub__btn--icon-primary pub__carousel__button pub__carousel__button--right" id="pub__-carousel__9f3727b0-202a-11ec-96f0-d900bf02a083-next-btn" type="button">
                <span class="pub__btn__inner">
                 <svg aria-hidden="true" class="pub__svg-icon pub__btn__icon" focusable="false" viewbox="0 0 24 24">
                  <path clip-rule="evenodd" d="m16.415 12.0011-8.0012 8.0007-1.4141-1.4143 6.587-6.5866-6.586-6.5868L8.415 4l8 8.0011z" fill-rule="evenodd">
                  </path>
                 </svg>
                </span>
               </button>
              </div>
              <div class="pub__scroll-indicator" tabindex="0">
              </div>
              <a id="pub__-carousel__9f3727b0-202a-11ec-96f0-d900bf02a083-skip-btn">
              </a>
             </div>
            </div>
           </div>
          </div>
         </div>
        </section>
       </div>
      </div>
     </div>
     <div class="plp-rec-panel-wrapper" data-catalog="fu001" data-mount-recommendations="plp-top">
     </div>
     <a name="product-list-skip">
     </a>
     <div class="plp-main-container">
      <noscript class="noscript-compact-fragments">
       <div class="plp-product-list">
        <div class="plp-product-list__products">
        </div>
       </div>
      </noscript>
     </div>
    </div>
   </div>
  </div>
  <!-- 2022-02-15T07:25:32.158Z, Navigera 2a15d589 -->
  <div data-recently-viewed="true">
  </div>
  <div class="hnf-sidebar-actions">
   <div class="hnf-sidebar-actions__inner">
    <div class="hnf-sidebar-actions__aside">
     <div class="hnf-sidebar-actions__bar" id="sidebar">
      <button class="hnf-btn hnf-btn--small hnf-btn--primary hnf-leading-icon hnf-btn--expanding hnf-btn--hidden hnf-sidebar-actions__back-to-top" id="btn-back-to-top" tabindex="-1" type="button">
       <span class="hnf-btn__inner">
        <svg class="svg-icon hnf-svg-icon hnf-btn__icon" fill="none" focusable="false" height="24" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
         <path clip-rule="evenodd" d="m12.0001 6.9394 8.0007 8.0013-1.4142 1.4141L12 9.7678l-6.5869 6.586-1.414-1.4143 8.001-8z" fill-rule="evenodd">
         </path>
        </svg>
        <span class="hnf-btn__label">
         Retour vers le haut
        </span>
       </span>
      </button>
      <button class="hnf-btn hnf-btn--small hnf-btn--primary hnf-leading-icon hnf-btn--expanding hnf-btn--hidden hnf-sidebar-actions__share-to-socialmedia js-btn-hnf-share-to-socialmedia" data-service="socialSharingPanel" type="button">
       <span class="hnf-btn__inner">
        <svg class="svg-icon hnf-svg-icon hnf-btn__icon" fill="none" focusable="false" height="24" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
         <path d="m11 7.8294-3.242 3.242-1.4143-1.4142L12 4l5.6575 5.6572-1.4143 1.4142L13 7.8284V16h-2V7.8294z">
         </path>
         <path d="M2 21.0029h20v-9h-2v7H4v-7H2v9z">
         </path>
        </svg>
        <span class="hnf-btn__label">
         Partager
        </span>
       </span>
      </button>
     </div>
    </div>
   </div>
  </div>
  <footer class="hnf-footer" role="contentinfo">
   <h-include-lazy src="https://www.ikea.com/ma/fr/header-footer/footer-lazy-fragment.html">
   </h-include-lazy>
  </footer>
  <!-- 2022-02-15T07:25:32.135Z, Navigera 2a15d589 -->
  <script src="https://polyfill.ikea.net/v3/polyfill.min.js?features=IntersectionObserver%2CObject.freeze%2Cdefault%2Ces2015%2Ces2016%2Ces2017%2Ces2018%2Ces2019%2Cfetch&amp;flags=gated">
  </script>
  <script data-client-id="6ef1a8c6-014d-4855-8309-fadab357777c" data-domain="www.ikea.com" data-intext="false" data-release="2a15d589" data-sentry="false" data-site-folder="ma/fr" id="nav-script-common" src="https://www.ikea.com/ma/fr/header-footer/javascripts/common.e1ad198d1a07815e6702.js">
  </script>
  <script src="https://www.ikea.com/ma/fr/header-footer/javascripts/main.2709a5a2236a3d7a0289.js">
  </script>
  <script async="" defer="defer" src="https://www.ikea.com/ma/fr/analytics/scripts/ga-main.a7a65c65.js">
  </script>
  <script async="" defer="defer" src="https://www.ikea.com/ma/fr/analytics/scripts/ga-targeting.a7a65c65.js">
  </script>
  <script async="" defer="defer" src="https://www.ikea.com/ma/fr/analytics/scripts/boomerang.min.js?a7a65c65841f4889afc6">
  </script>
  <script>
   window.isLandingPage =
    document.referrer.split('/')[2] !== location.host ? true : false;
  window.analyticsQueue = window.analyticsQueue || [];
  window.sendEvent = function (evt) {
    window.analyticsQueue.push(evt);
  };

  window.ikea.analytics = {
    observeProducts: [],
    observeProductDetails: [],
  };
  </script>
  <!-- Search Box Scripts: 2022-02-11 7:54:07 CET refs/tags/v8.200.0-3d21032ab0cf4bf06e56d7f2934eb683a2957c59 -->
  <link crossorigin="" href="https://sik.search.blue.cdtapps.com" rel="preconnect"/>
  <script>
   function search_addScript(src, legacy) {
    var script = document.createElement('script')
    if (!legacy) {
      script.setAttribute('type', 'module')
      
    }
    script.setAttribute('src', "https://www.ikea.com" + src)
    document[legacy ? 'body' : 'head'].appendChild(script)
  }
  if ('noModule' in HTMLScriptElement.prototype && CSS.supports('image-orientation: none') && 'fromEntries' in Object) { //check if modern enough
    
      search_addScript("/ma/fr/search/shared.a1aa2c5b.js")
    
    
      search_addScript("/ma/fr/search/search_vendors.a1aa2c5b.js")
    
    
      search_addScript("/ma/fr/search/box.a1aa2c5b.js")
    
  } else {
    
      search_addScript("/ma/fr/search/box-legacy.a1aa2c5b.js", true)
    
  }
  </script>
  <!-- /Search Box Scripts -->
  <!-- RecommendationsScript: version: 6b92168, site-folder: ma/fr -->
  <script>
   if (window && window.ikea && window.ikea.sentry && window.ikea.sentry.register) {
    window.ikea.sentry.register('5583489', '10bb11cc3ff548e295b5e960579d8042', 'recommendations', '6b92168', 0.1, [/\/[a-z0-9]{2}\/[a-z0-9]{2}\/recommendations\/panels\//]);
  }
  </script>
  <script defer="defer" src="https://www.ikea.com/ma/fr/recommendations/panels/events.b208a147.js" type="module">
  </script>
  <script defer="defer" src="https://www.ikea.com/ma/fr/recommendations/panels/rec.b208a147.js" type="module">
  </script>
  <!-- /RecommendationsScript -->
  <!-- gitVersion: refs/tags/v0.2.0, siteFolder: ma/fr -->
  <script defer="defer" src="https://www.ikea.com/ma/fr/purchase-agent/cart-tmp/vendor.ba42690b.js">
  </script>
  <script defer="defer" src="https://www.ikea.com/ma/fr/purchase-agent/cart-tmp/purchase-middleware-base.30d4d6ae.js">
  </script>
  <!-- igift-agent-disabled -->
  <!--
  Navigera Sentry helper: https://confluence.build.ingka.ikea.com/display/CMPWEB/Navigera%3A+Sentry+helper
  Feed gitVersion: 20220214052700, siteFolder: ma/fr
-->
  <script>
   if (window && window.ikea && window.ikea.sentry && window.ikea.sentry.register) {
    window.ikea.sentry.register(
      '5244394', // The Sentry project ID
      '4def75a18cb34ab59e68a690be123979', // The Sentry project key
      'feed', // The product name
      '20220214052700', // The product release version
      0.1, // 10% sample rate
      [/\/[a-z0-9]{2}\/[a-z0-9]{2}\/insp-feed\/content-gallery-app\//] // Paths to register for errors in
    );
  }
  </script>
  <script defer="defer" src="https://www.ikea.com/ma/fr/insp-feed/content-gallery-app/feed.b7bf7399.js">
  </script>
  <script src="https://www.ikea.com/ma/fr/products/javascripts/price-package-scripts.e8cfb34f7b9e8b6e88fc.js">
  </script>
  <script src="/ma/fr/javascripts/main.5cd07f836a0c276ae6fb.js">
  </script>
  <script src="/ma/fr/javascripts/vendors.d63a6da1f93ea2862282.js">
  </script>
  <script type="text/javascript">
   window["optimizelyDatafile"] = {"version": "4", "rollouts": [], "typedAudiences": [], "anonymizeIP": true, "projectId": "18201302387", "variables": [], "featureFlags": [], "experiments": [], "audiences": [{"conditions": "[\"or\", {\"match\": \"exact\", \"name\": \"$opt_dummy_attribute\", \"type\": \"custom_attribute\", \"value\": \"$opt_dummy_value\"}]", "id": "$opt_dummy_audience", "name": "Optimizely-Generated Audience for Backwards Compatibility"}], "groups": [], "sdkKey": "B55RSZvdcuDQ8kD1YxvvN", "environmentKey": "production", "attributes": [{"id": "18219820812", "key": "marketCode"}, {"id": "18716282466", "key": "site"}, {"id": "18724591472", "key": "environment"}, {"id": "18743753042", "key": "url"}, {"id": "18749011620", "key": "browser"}, {"id": "18754351030", "key": "position"}, {"id": "18764370003", "key": "device"}, {"id": "18779380060", "key": "market"}, {"id": "19402671474", "key": "plp-environment"}, {"id": "19406141378", "key": "plp-marketCode"}, {"id": "19406563217", "key": "plp-browser"}, {"id": "19408102758", "key": "plp-device"}, {"id": "19425931423", "key": "plp-position"}, {"id": "19433182009", "key": "plp-market"}, {"id": "19459171443", "key": "plp-site"}, {"id": "19477101023", "key": "plp-url"}, {"id": "19862691877", "key": "plp-category-id"}, {"id": "20191982540", "key": "plp-category-type"}, {"id": "20909790215", "key": "plp-is-pax-system"}], "botFiltering": true, "accountId": "11701662245", "events": [{"experimentIds": [], "id": "20262589732", "key": "plp_enhanced_product_add_to_favourites"}, {"experimentIds": [], "id": "20272779632", "key": "plp_variant_click_card"}, {"experimentIds": [], "id": "20282776408", "key": "plp_product_add_to_cart"}, {"experimentIds": [], "id": "20286425907", "key": "plp_filter_clear_all"}, {"experimentIds": [], "id": "20286851473", "key": "plp_activate_experiment"}, {"experimentIds": [], "id": "20292354803", "key": "plp_visit_page_plp"}, {"experimentIds": [], "id": "20292483563", "key": "plp_sort_selected"}, {"experimentIds": [], "id": "20294664853", "key": "plp_filter_deselected"}, {"experimentIds": [], "id": "20294664874", "key": "plp_planner_click_through"}, {"experimentIds": [], "id": "20296595467", "key": "plp_filter_selected"}, {"experimentIds": [], "id": "20296813297", "key": "plp_compare_activate"}, {"experimentIds": [], "id": "20300463897", "key": "plp_shoppable_image_product_click"}, {"experimentIds": [], "id": "20303695510", "key": "plp_sort_open"}, {"experimentIds": [], "id": "20303863636", "key": "plp_more_filters_clicked"}, {"experimentIds": [], "id": "20305277698", "key": "plp_compare_navigate"}, {"experimentIds": [], "id": "20305277701", "key": "plp_enhanced_product_click_through"}, {"experimentIds": [], "id": "20307665112", "key": "plp_applied_filter_deselected"}, {"experimentIds": [], "id": "20308100707", "key": "plp_shoppable_image_click"}, {"experimentIds": [], "id": "20311305394", "key": "plp_filter_open"}, {"experimentIds": [], "id": "20311682614", "key": "plp_variant_view"}, {"experimentIds": [], "id": "20311791546", "key": "plp_product_add_to_favourites"}, {"experimentIds": [], "id": "20313374285", "key": "plp_variant_click"}, {"experimentIds": [], "id": "20314080646", "key": "plp_applied_filter_clear_all"}, {"experimentIds": [], "id": "20315483428", "key": "plp_element_visible"}, {"experimentIds": [], "id": "20316400045", "key": "plp_enhanced_product_add_to_cart"}, {"experimentIds": [], "id": "20317224557", "key": "plp_callout_click_through"}, {"experimentIds": [], "id": "20319083610", "key": "plp_product_click_through"}, {"experimentIds": [], "id": "20330152316", "key": "plp_bottom_navigation_click"}, {"experimentIds": [], "id": "20333695755", "key": "plp_quick_filter_click"}, {"experimentIds": [], "id": "20355940487", "key": "plp_filter_description_click"}, {"experimentIds": [], "id": "20870241457", "key": "plp_content_view"}, {"experimentIds": [], "id": "20895670187", "key": "plp_top_navigation_click"}, {"experimentIds": [], "id": "20920990010", "key": "plp_content_click"}, {"experimentIds": [], "id": "20945720996", "key": "plp_content_expand"}, {"experimentIds": [], "id": "21146010233", "key": "plp_product_list_view"}], "revision": "708"}
  </script>
  <script src="https://www.ikea.com/ma/fr/product-lists/plp-main-716.js">
  </script>
  <!-- 2022-02-15T07:25:32.136Z, Navigera 2a15d589 -->
  <script async="" src="https://www.ikea.com/ma/fr/local-extensions/header-footer/scripts/a4g.89c27976b4cc7265ae32c037.js">
  </script>
  <script async="" src="https://www.ikea.com/ma/fr/local-extensions/header-footer/scripts/gtag.d8cdc11a23ffeb46fa02c96b.js">
  </script>
  <script async="" src="https://www.ikea.com/ma/fr/local-extensions/header-footer/scripts/bluecore.ba449b02a0fb4d463501f7a2.js">
  </script>
  <!-- Facebook - Global -->
  <script async="" src="https://www.ikea.com/ma/fr/local-extensions/header-footer/scripts/facebook-global.fdaf0e710a0131277b35a696.js">
  </script>
  <noscript>
   <img height="1" src="https://www.facebook.com/tr?id=758024975074856&amp;ev=PageView&amp;noscript=1" style="display:none" width="1"/>
  </noscript>
  <!-- Facebook - Local -->
  <script async="" src="https://www.ikea.com/ma/fr/local-extensions/header-footer/scripts/facebook.9cce88454e6c4c48039bc9fd.js">
  </script>
  <noscript>
   <img height="1" src="https://www.facebook.com/tr?id=292551595001418&amp;ev=PageView&amp;noscript=1" style="display:none" width="1"/>
  </noscript>
  <!--Hotjar-->
  <script>
   (function(h,o,t,j,a,r){
      h.hj=h.hj||function(){(h.hj.q=h.hj.q||[]).push(arguments)};
      h._hjSettings={hjid:2308668,hjsv:6};
      a=o.getElementsByTagName('head')[0];
      r=o.createElement('script');r.async=1;
      r.src=t+h._hjSettings.hjid+j+h._hjSettings.hjsv;
      a.appendChild(r);
  })(window,document,'https://static.hotjar.com/c/hotjar-','.js?sv=');
  </script>
  <script src="https://www.ikea.com/B4kom28tdnUP/7c/o81Yky4Ut4/X1zODQ3QD1Eu/PxVSYg/ZSxnTzU/LPWg" type="text/javascript">
  </script>
 </body>
</html>
"""

items = BS(html, features="html.parser")

l = list()
links = items.findAll('a' , {'class' : 'vn-link vn__nav__link vn-6-grid-gap'})
for link in links:
    d = dict()
    d["link"] = link.get('href')
    f[""]

print(l)