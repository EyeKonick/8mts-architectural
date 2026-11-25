const sharp=require('sharp');const I='images/',O='src/assets/images/',A='assets/img/';
(async()=>{
 await sharp(I+'895915392_122105938167539257_65874946386374915_n.jpg').extract({left:0,top:0,width:2000,height:1090}).jpeg({quality:84}).toFile(O+'condo-interior.jpg');
 await sharp(I+'896292023_122105858607539257_6095916734250404732_n.jpg').extract({left:930,top:640,width:1070,height:1330}).jpeg({quality:84}).toFile(O+'house-exterior.jpg');
 await sharp(I+'897874840_122105948139539257_7561889882216717042_n.jpg').extract({left:1012,top:0,width:988,height:2000}).jpeg({quality:84}).toFile(O+'asbuilt-plans.jpg');
 for (const [s,n] of [['photo-f151572322.jpg','massing-model.jpg'],['photo-f151572530-960.jpg','villa-model.jpg'],['photo-f184252234-500.jpg','blueprint-small.jpg'],['photo-f171129895.jpg','floor-plan.jpg']]) await sharp(A+s).toFile(O+n);
 // logo -> transparent black PNG (alpha from darkness), trimmed
 const {data,info}=await sharp(I+'848438858_122106371355526808_2129950896849540246_n.jpg').greyscale().raw().toBuffer({resolveWithObject:true});
 const rgba=Buffer.alloc(info.width*info.height*4);
 for(let i=0;i<info.width*info.height;i++){const a=255-data[i];rgba[i*4]=0;rgba[i*4+1]=0;rgba[i*4+2]=0;rgba[i*4+3]=a<20?0:Math.min(255,a*1.1);}
 await sharp(rgba,{raw:{width:info.width,height:info.height,channels:4}}).trim().png().toFile('.taste-skill/logo-full.png');
 const m=await sharp('.taste-skill/logo-full.png').metadata();console.log('logo',m.width,m.height);
})();
