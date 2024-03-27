function mouse_pressed() {
    if (hit_colour === Color('blue').hex) {
        console.log('🎯 You hit the outer circle, 50 points!');
    } else if (hit_colour === Color('red').hex) {
        console.log('🎯 You hit the inner circle, 200 points!');
    } else if (hit_colour === Color('yellow').hex) {
        console.log('🎯 You hit the middle, 500 points!');
    } else {
        console.log('You loose! No points!');
    }
}

function shoot_arrow() {
    var hit_colour;
    var arrow_x = Math.floor(Math.random() * (300 - 100 + 1) + 100);
    var arrow_y = Math.floor(Math.random() * (300 - 100 + 1) + 100);
    hit_colour = get(arrow_x, arrow_y).hex;

    fill('sienna');
    circle(arrow_x, arrow_y, 15);
}

function setup() {
    size(400, 400);
    no_stroke();
}

function draw() {
    fill('cyan');
    rect(0, 0, 400, 250);
    fill('lightgreen');
    rect(0, 250, 400, 150);
    fill('sienna');
    triangle(150, 350, 200, 150, 250, 350);
    fill('blue');
    circle(200, 200, 170);
    fill('red');
    circle(200, 200, 110);
    fill('yellow');
    circle(200, 200, 30);
    shoot_arrow();
}

run({ frame_rate: 2 });

