// Cat.js

class Cat extends Phaser.Physics.Arcade.Sprite {
    constructor(scene, x, y) {
        super(scene, x, y, 'cat');
        scene.add.existing(this);
        scene.physics.add.existing(this);

        this.setCollideWorldBounds(true);
        this.length = gameSettings.initialCatLength;
    }

    update() {
        if (this.scene.input.activePointer.isDown) {
            this.length += 0.1; // Example logic for increasing length
        } else {
            this.length -= 0.1; // Example logic for decreasing length
        }

        this.length = Phaser.Math.Clamp(this.length, 1, gameSettings.maxCatLength);
    }
}
