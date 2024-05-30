// GameScene.js

class GameScene extends Phaser.Scene {
    constructor() {
        super('GameScene');
    }

    create() {
        this.add.image(400, 300, 'background');
        this.cat = new Cat(this, 400, 300);
        this.obstacles = this.physics.add.group();

        // Example of creating obstacles
        this.obstacles.create(600, 400, 'obstacle');

        // Collision detection
        this.physics.add.collider(this.cat, this.obstacles, this.hitObstacle, null, this);
    }

    update() {
        this.cat.update();
    }

    hitObstacle(cat, obstacle) {
        this.scene.start('EndScene');
    }
}
