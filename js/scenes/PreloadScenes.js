// PreloadScene.js

class PreloadScene extends Phaser.Scene {
    constructor() {
        super('PreloadScene');
    }

    preload() {
        this.load.image('cat', 'assets/images/cat.png');
        this.load.image('obstacle', 'assets/images/obstacle.png');
        this.load.image('powerup', 'assets/images/powerup.png');
        this.load.image('background', 'assets/images/background.png');
    }

    create() {
        this.scene.start('MenuScene');
    }
}
