console.log("Hello world");


// ///////////////////////////// category filters
const filterItems = document.querySelectorAll(".buttons .filter-items");

const toggleClassItem = (items, item, className)=>{
    if(item.hasAttribute("data-id")){
        const id = item.getAttribute("data-id");
        console.log(id);
    }

    if(!item.classList.contains(className))
    {
        items.forEach(i => i.classList.remove(className));
        item.classList.add(className);
    }
}

filterItems.forEach(item => {
    item.addEventListener("mousedown", ()=>{
        toggleClassItem(filterItems, item, "active");
    });
})


// ///////////////////////////// categories
const subCategoryItems = document.querySelectorAll("aside.categories .sub-category");

subCategoryItems.forEach(item => {
    const elem = item.getElementsByClassName("sub-category-item")[0];
    elem.addEventListener("mousedown", ()=>{
        toggleCategoryItem(item, "active");
    });
})

const toggleCategoryItem = (item, className)=>{
    //categoryItems.forEach(i => i.classList.remove(className));

    if(item.classList.contains(className)){
        console.log("is active");
        item.classList.remove(className);
    }else{
        item.classList.add(className);
        console.log("not active");
    }

    // console.log(className);
}

const categoryItems = document.querySelectorAll("aside.categories .category-item");

// const headlines = document.getElementById("category-filter");

categoryItems.forEach(item => {
    item.addEventListener("mousedown", ()=>{
        toggleClassItem(categoryItems, item, "current");

        const escape = "&#10095;";
        const parentItem = item.parentElement.previousElementSibling;
        
        subCategoryItems.forEach(i => {
            if(i.getElementsByTagName("p").length > 0){
                const actionP = i.getElementsByTagName("p")[0];
                actionP.classList.remove("active");
            }
        });
        let category = "";
        const dataName = "data-name";

        if(parentItem){
            parentItem.classList.add("active");
            category = parentItem.getAttribute(dataName);
            category += escape;
        }

        category += item.getAttribute(dataName);
        
        // headlines.querySelector(".cat").innerHTML = category;
        console.log("Category: ", category);
    });
})

////////////////////////// add to cart

const addToCartButton = document.querySelector("#add-to-cart");

if(addToCartButton){
    addToCartButton.addEventListener("mousedown", (event)=>{
        // event.preventDefault();
     
         console.log("add to cart");
     })
}

///////////////////////// scrolling scroller
const scroller = document.querySelector("#scroller");

window.addEventListener("scroll", ()=>{
    const scrollPos = window.scrollY || (document.documentElement || document.body.parentNode || document.body).scrollTop;
    const screenSize = window.innerHeight || (document.documentElement || document.body).clientHeight;

    if(scrollPos >= screenSize)
    {
        if(!scroller.classList.contains("show")){
            scroller.classList.add("show");
        }
    }else{
        if(scroller.classList.contains("show")){
            scroller.classList.remove("show");
        }
    }
    console.log("pos: ", 
    document.documentElement.scrollTop,
    ", screen size: ", screenSize);
});

scroller.addEventListener("mousedown", ()=>{
    window.scrollTo({top: 0});
})

//// toggle side bar
const sideBar = document.querySelector("section.side-bar");
const hurmburger = document.querySelector("#humburger");


class ToggleElements{
    constructor(){
        this.element = null;
        this.className = "";
    }

    setClassName(name){
        this.className = name;
    }

    setElement(elem){
        this.element = elem;
    }

    toggleClassName() {
        if(!this.element){
            return;
        }
        const cls = this.element.classList;
        if(cls.contains(this.className)){
            this.element.classList.remove(this.className);
        }else{
            this.element.classList.add(this.className);
        }
    }

    toggleClassNameInItems(htmlElements){
        if(!this.element || !Array.isArray(htmlElements) || htmlElements.length <= 0){
            return;
        }

        htmlElements.forEach((item)=>{
            if(item.classList.contains(this.className)){
                item.classList.remove(this.className);
            }
        });

        // now all elements does not have className 
        this.element.classList.add(this.className);
    }
}

const closeSideBarBtn = document.getElementById("close-side-bar");
const toggle = new ToggleElements();

hurmburger.addEventListener("click", ()=>{
    toggle.setClassName('active');
    toggle.setElement(sideBar);
    toggle.toggleClassName();
});

closeSideBarBtn.addEventListener("click", ()=>{
    toggle.setClassName('active');
    toggle.toggleClassName();
})

window.addEventListener("click", (e)=>{
    console.log("hellow");
    if(e.target.id === 'side-bar'){
        console.log("inside");
    }
})