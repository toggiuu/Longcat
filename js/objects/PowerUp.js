// PowerUp.js

class PowerUp extends Phaser.Physics.Arcade.Sprite {
    constructor(scene, x, y) {
        super(scene, x, y, 'powerup');
        scene.add.existing(this);
        scene.physics.add.existing(this);

        this.setImmovable(true);
    }

    applyEffect(cat) {
        // Example logic for applying power-up effect
        cat.length += 5;
    }
}
