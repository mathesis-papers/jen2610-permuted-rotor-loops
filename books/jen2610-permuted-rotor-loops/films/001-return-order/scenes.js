'use strict';

function filmHeading(heading, subheading) {
  txt(heading, W / 2, 204, {size: 64, w: 800, c: C.white, align: 'center'});
  txt(subheading, W / 2, 280, {size: 34, w: 600, c: C.cyan, align: 'center'});
}

function orderRows(outward, returning, opacity) {
  panel(310, 352, 1300, 360, opacity, C.cyan);
  txt('OUTWARD', 425, 472, {size: 30, w: 700, c: C.cyan, a: opacity});
  txt('RETURN', 425, 617, {size: 30, w: 700, c: C.now, a: opacity});
  outward.forEach((index, position) => chip(760 + position * 235, 402, 185, 100, String(index), C.cyan, opacity, 52));
  returning.forEach((index, position) => chip(760 + position * 235, 547, 185, 100, String(index), C.now, opacity, 52));
}

FILM.poster = () => {
  filmHeading('Changing the return order', 'Which pairs keep their order?');
  orderRows([1, 2, 3], [2, 1, 3], 1);
  txt('Haobo Ma and Wenlin Zhang  /  Version 5', W / 2, 839, {size: 30, c: C.white, align: 'center'});
};

SCENES.triangle = scene => {
  filmHeading('Three turning planes', 'Reverse order cancels; a different order need not.');
  orderRows([1, 2, 3], [2, 1, 3], 1);
  txt('B₁ B₂ B₃ = −1  ·  the star condition fails', W / 2, 835,
      {size: 44, w: 700, c: C.now, a: at(scene, 1, 0.5), align: 'center'});
};

SCENES.pairs = scene => {
  filmHeading('Count unchanged pairs', 'Return order: 2, 1, 3      Pairs: {1, 3}, {2, 3}');
  const firstReveal = at(scene, 1, 0.55);
  const secondReveal = at(scene, 2, 0.55);
  panel(270, 349, 1380, 203, firstReveal, C.cyan, 'WITHOUT 3');
  panel(270, 584, 1380, 203, secondReveal, C.now, 'WITH 3');
  ['+1', '+1', '+1', '+1'].forEach((sign, position) => chip(616 + 204 * position, 433, 145, 70, sign, C.cyan, firstReveal, 40));
  ['+1', '−1', '−1', '+1'].forEach((sign, position) => chip(616 + 204 * position, 662, 145, 70, sign, C.now, secondReveal, 40));
  txt('Average sign: 1/2', W / 2, 859, {size: 44, w: 700, c: C.white, a: secondReveal, align: 'center'});
};

SCENES.cancel = scene => {
  filmHeading('The odd terms cancel together', 'Only complementary subsets can contribute an exceptional term.');
  const swap = at(scene, 1, 0.6);
  const parity = at(scene, 2, 0.6);
  panel(210, 363, 1500, 206, swap, C.cyan, 'EXTERIOR SWAP');
  txt('(1 + x)(1 + y) = (1 + 2xy)(1 + y)(1 + x)', W / 2, 493,
      {size: 52, c: C.white, a: swap, align: 'center'});
  panel(210, 612, 1500, 180, parity, C.now, 'AFTER REVERSE CANCELLATION');
  txt('Even factors only   →   every odd coefficient is zero', W / 2, 721,
      {size: 39, c: C.white, a: parity, align: 'center'});
};

SCENES.close = scene => {
  filmHeading('The loop is not the chain', 'No star condition for the scalar loop formula.');
  panel(345, 405, 1230, 252, 1, C.cyan, 'SQUARE-MINUS-ONE BIVECTORS');
  txt('Every return permutation', W / 2, 553, {size: 69, w: 800, c: C.white, align: 'center'});
  txt('Ma & Zhang  ·  Version 5  ·  Theorem 1', W / 2, 784,
      {size: 36, a: at(scene, 0, 0.8), c: C.cyan, align: 'center'});
};
