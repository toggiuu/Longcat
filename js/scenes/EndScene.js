// EndScene.js

class EndScene extends Phaser.Scene {
    constructor() {
        super('EndScene');
    }

    create() {
        this.add.text(400, 300, 'Game Over', { fontSize: '64px', fill: '#fff' }).setOrigin(0.5);
        this.add.text(400, 400, 'Click to Restart', { fontSize: '32px', fill: '#fff' }).setOrigin(0.5);

        this.input.on('pointerdown', () => {
            this.scene.start('MenuScene');
        });
    }
}
