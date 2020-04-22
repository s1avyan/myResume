$(document).ready(function () {
  let cashInWallet = 10;
  let age = 18;
  let cardAmount = 50;
  const price = 40;
  const ageLimit = 18;

  const canPayWithCard = cardAmount >= price;
  const isAllowed = age >= ageLimit;
  const hasEnoughMoney = cashInWallet >= price;

  const canBuy = (isAllowed && hasEnoughMoney) || (isAllowed && canPayWithCard);
  console.log(canBuy);
});
