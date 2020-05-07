$(document).ready(function () {
  // настройки сликслайдера
  $('.slider').slick({
    arrows: false,
    dots: true,
    adaptiveHeight: false,
    autoplay: true,
    autoplaySpeed: 5000,
    centerMode: false,
    speed: 1000,
    variableWidth: false,
  });
  // настройки сликслайдера

  $('.header__burger').click(function (event) {
    $('.header__burger').toggleClass('active');
  });
});

// тренировка CODEWARS 7kyu
// сложение двух меньших значений списка
x = [1, 3, 7, 2, 11, 5];
function sumTwoSmallestNumbers(numbers) {
  var numbers = numbers.sort(function (a, b) {
    return a - b;
  });
  answer = numbers[0] + numbers[1];
  // console.log('Answer is :=> ' + answer);
}
sumTwoSmallestNumbers(x);
// тренировка CODEWARS 8kyu (Remove String Spaces)
string = "8 j 8   mBliB8g  imjB8B8  jl  B'), '8j8mBliB8gimjB8B8jlB";
function noSpace(string_to_split, separator) {
  var arrayOfStrings = string_to_split.split(separator);
  console.log('Оригинальная строка: "' + string_to_split + '"');
  console.log('Разделителем назначили: "' + separator + '"');
  console.log('Массив содержит: ' + arrayOfStrings.length + ' элементов' + arrayOfStrings.join(' / '));
}
sep = ' ';
noSpace(string, ' ');
