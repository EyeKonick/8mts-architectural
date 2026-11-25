const s=require('sharp');
(async()=>{for(const w of [390]){const f=`shots/s${w}.png`;const {data,info}=await s(f).raw().toBuffer({resolveWithObject:true});
let start=-1,end=-1;for(let y=0;y<info.height;y++){const i=(y*info.width+5)*info.channels;const r=data[i],g=data[i+1],b=data[i+2];const green=Math.abs(r-0x2b)<6&&Math.abs(g-0x3f)<6&&Math.abs(b-0x1f)<6;if(green&&start<0)start=y;if(green)end=y;}
console.log(w,start,end);await s(f).extract({left:0,top:start,width:info.width,height:end-start+1}).resize(700).jpeg({quality:75}).toFile(`.taste-skill/stmt-${w}.jpg`);}})();
