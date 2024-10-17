const leftEl = document.querySelectorAll(".left");
const rightEl = document.querySelectorAll(".right");
const contEl = document.querySelectorAll(".cont");

window.addEventListener("scroll",()=>{
    let i = 0;
    let j = 1;

    
        leftEl.forEach((e)=>{
            
            if(window.pageYOffset || document.documentElement.scrollTop >320){
               
                e.style.animation = "contdown 1s ease-in forwards";
                // console.log(i);
                e.style.animationDelay=`${i}s`;
                i = i+2;
                
            }
    
        })
        rightEl.forEach((e)=>{
           
            if(window.pageYOffset || document.documentElement.scrollTop >320){
                e.style.animation = "contdown2 1s ease-in forwards";
                // console.log(j);
                e.style.animationDelay=`${j}s`;
                j=j+2;
            }
    
        })

        

    })


    const prevBtn = document.querySelector(".prev-btn");
const nextBtn = document.querySelector(".next-btn");
const imageContainer = document.querySelector(".image-container");

const imgEls = document.querySelectorAll(".slide-image");
console.log(imgEls.length);
let counter = 1;

let timeout;

nextBtn.addEventListener("click",()=>{
    counter++;
    clearTimeout(timeout);
    updateImage();

})

prevBtn.addEventListener("click",()=>{
    counter--;
    clearTimeout(timeout);
    updateImage();

})



const updateImage = () =>{
    if(counter>imgEls.length){
        counter = 1;
    }else if(counter<1){
        counter = imgEls.length;
    }

    imageContainer.style.transform = `translateX(-${(counter - 1) * 540}px)`;

    timeout = setTimeout(()=>{
        counter++;
        updateImage();
    },5000);

    
}
updateImage();
    
    
