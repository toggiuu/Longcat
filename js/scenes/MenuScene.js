// MenuScene.js

class MenuScene extends Phaser.Scene {
    constructor() {
        super('MenuScene');
    }

    create() {
        this.add.text(400, 300, 'Longcat', { fontSize: '64px', fill: '#fff' }).setOrigin(0.5);
        this.add.text(400, 400, 'Click to Start', { fontSize: '32px', fill: '#fff' }).setOrigin(0.5);

        this.input.on('pointerdown', () => {
            this.scene.start('GameScene');
        });
    }
}
