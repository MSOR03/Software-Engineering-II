// OCP - Open/Closed Principle
// Abierto a extensión, cerrado a modificación.

const discountStrategies = {
  regular: (price) => price * 0.9,
  vip: (price) => price * 0.8,
};

function calculateDiscount(type, price) {
  const strategy = discountStrategies[type];
  if (!strategy) {
    throw new Error("Tipo de descuento no soportado");
  }
  return strategy(price);
}

console.log("Regular:", calculateDiscount("regular", 100));
console.log("VIP:", calculateDiscount("vip", 100));

// Extensión sin tocar calculateDiscount
discountStrategies.premium = (price) => price * 0.7;
console.log("Premium:", calculateDiscount("premium", 100));
