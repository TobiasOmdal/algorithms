//Receives to IP-addresses and finds how many
//places are between the two IPs, given that 
//every slot goes from 0 to 255 and each slot 
//is 255 times the previous.  
function ipsBetween(start, end){
    //declares two sum variables
    let sum1 = 0, sum2 = 0; 
    //Maps over the reverse array of numbers
    //and adds the value times 256 to the power of 
    //the index. 
    start.split(".").reverse().map((n, index) => {
        sum1 += n*(256**index);
    });
    //Does the same for the other IP
    end.split(".").reverse().map((n, index) => {
        sum2 += n*(256**index);
    });
    //returns the difference in sums
    return sum2 - sum1;
}

console.log(ipsBetween("20.0.0.10", "20.0.1.0")===246);