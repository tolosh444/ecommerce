function removeRow(rowID) {
    $(`${rowID}`).remove();

}


function calcTotal(ID) {
    let price = document.getElementById(`price-${ID}`).innerText;
    let quantity = document.getElementById(`qty-${ID}`).value;
    console.log('price',price);
    console.log('qty', quantity);
    let result = document.getElementById(`total-${ID}`).innerHTML = (parseFloat(price) * parseFloat(quantity));
    console.log(result);
}