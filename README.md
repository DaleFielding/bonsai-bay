# Bonsai Bay
The purpose of this site is to provide a platform for bonsai enthusiasts, both individuals and businesses, to digitally market their bonsai trees or browse and purchase trees listed on the website. It will feature a relational database designed to store all relevant information necessary for the site's operation.

(Heroku link to be added)

(Mock-up image to be added)

## User Experience (UX)

### User Stories
1. As a user, I would like to access a digital marketplace specifically for the sale and purchase of bonsai trees.
2. As a user, I would like to be able to create an account where I can store my information.
3. As a user, I would like to be able to create and display listings for sale and manage these by amending or deleting.
4. As a user, I would like to view/search for bonsai trees on the site that people would like to sell.
5. As a user, I would like to view information about the product such as; product, description, location etc.
6. As a user, I would like to filter items to refine my search.
7. As a user, I would like to be able to contact the seller.

### Site Objectives
1. To appeal to bonsai enthusiasts and potential bonsai enthusiasts of any age.
2. To be responsive and functional.
3. To meet all accessibility requirements, allowing anyone to use the site regardless of their abilities/needs.
4. To include an appropriate data model for the website, that functions as intended.

## Design
### Strategy 
Taking into account the intended website, I have:

* Conducted research into websites that offer bonsai related services:
  * [Greenwood Bonsai Studio](https://www.bonsai.co.uk/)
  * [Herons Bonsai](https://www.herons.co.uk/)
  * [Bonsai2U](https://bonsai2u.co.uk/)
  * [British Bonsai](https://britishbonsai.co.uk/)<br>
  
  General findings with these sites are:
    * Logo is positioned in the top left. 
    * Most contain a search function.
    * Most have contact details displayed at the top of the page also.
    * The majority tend to white and green as the main colours for the site. In some there is the use of cream and various shades of grey. There is another site that uses red and white as the main colours.
    * All the sites contain the navigation at the top of the page, which generally includes; categories for bonsai trees, links to products or services within the site.
    * All have sections to login/register an account. 
    * All have shopping carts where items can be added to purchase.
    * They contain a banner/main image(s) directly below the navigation, which draw the visitors attention. These contain headers and some contain animations or buttons.
    * All display images of the products through the sites in a grid or various different sizes, these also show the item name and price.
    * When a bonsai tree is clicked this expands to provide more information, such as; species, price,  height, desired location, and general maintenance.
    * Some have additional selling points such as an introduction/reasons to choose them, reviews, testimonials or mention of affiliations with reputable companies.
    * Footers contain links for site navigation, social media, FAQs/help. Also contains contact details.

* Conducted research into digital marketplaces with similar functionality that I would like to achieve within the website:
  * [Gumtree](https://www.gumtree.com/)
  * [Facebook Marketplace](https://www.facebook.com/marketplace/)

  General findings with these sites are:
    * Similar navigation design to the bonsai sites in terms of logo, search function, account register/login.
    * There are also buttons to sell/create a new listing.
    * Also Images of items for sale are displayed as a grid and include; price, item name, location and some have brief descriptions.
    * When an item is clicked this takes you to more information about the item, such as further images or description. It also provides the options to add to saved items, share, or contact the seller.  (messenger, whatsapp or email). There is also a map to display an approximate location.
    * These sites contain ways to filter/refine a search, which is displayed down the left of the page.
    * They have location finding logic and the option to choose other locations.
    * I don’t believe Facebook marketplace has a footer and just seems to continue displaying further items as you scroll down.
    * Gumtree contains a similar footer to that of the bonsai sites, but also contains a link to download their app.

Following on from research, the strategy is to create a website that combines the feel of a bonsai site but with the functionality of a popular digital marketplace. The site should meet all of the expectations from the user stories, site objectives while also considering findings from the research conducted. 

### Scope
I have listed the possible features below and ranked 1-5 in level of importance/relevance to user needs (1 being most important and viable/feasible):

| Possible Feature | Rank |
|---|---|
| Site navigation | 1 |
| Accessibility | 1 |
| Device/resolution responsivity | 1 |
| Responses to user action | 1 |
| Account login and account management | 1 |
| Ability to create, update and delete listings | 1 |
| Location finding | 1 |
| Images of items for sale including relevant information | 1 | 
| Method to contact seller | 1 |
| Ability to save items | 1 |
| 404 page | 1 |
| Introduction with background image | 1 | 
| Ability to choose location | 2 |  
| Search function | 2 |
| Filters to refine search; such as distance, type or price | 2 |
| Ability to navigate by categories | 2 |
| Footer | 3 |
| Logo | 3 |
| Social links | 3 |
| Instant Messenger between buyer and seller | 3 |
| Reviews | 5 | 
| Blog | 5 |  

As some of these features extend beyond the necessary requirements for the project and may take more time than appropriate, I will not will not currently be implementing:
* Instant messenger
* Reviews
* Blog 

### Structure 
I have listed the pages below including the features they will contain. 

#### All pages:
 * Navbar:
  * Logo and site name, clicking on these will reload the home page.
  * Search bar/function. 
  * Location selection.
  * Account button.
 * Navigation by category.
 * Footer:
   * Social media links.
   * Help/Contact Us.
   * Categories.	

#### Homepage:
* Introduction with background image.  
* Images of items for sale including relevant information. 
* Item filters. 
* Save item button. 

#### Item Page:
* Method to contact seller. 
* More information relating to the item.
* Save item button. 

#### Account Page:
* Account details (expands when clicked):
  * Email displayed.
  * Password change.
* Listings button (expands when clicked):
  * Create listings, clicking on this displays a modal for the data entry.
  * Shows listings.
  * View button. 
  * Amend button. 
  * Delete button.
* Saved items button (expands when clicked):
  * Shows saved items. 
  * View button. 
  * Remove button.  

#### 404 page:
* Message displayed confirming user has tried to visit a page in the domain that does not exist.
* Link/button within the page content that will direct the user to the home page.

### Skeleton

#### Table Schema

![Table schema](resources/table-schema.png)

#### Wireframes

  <details><summary>Homepage</summary>
    <img src="resources/wireframe-homepage.png">
  </details>

  <details><summary>Homepage With Model</summary>
    <img src="resources/wireframe-homepage-with-model.png">
  </details>
  
  <details><summary>Item Page</summary>
    <img src="resources/wireframe-item-page.png">
  </details>

  <details><summary>Account Page</summary>
    <img src="resources/wireframe-account-page.png">
  </details>

  <details><summary>404 page</summary>
    <img src="resources/wireframe-404-page.png">
  </details>
