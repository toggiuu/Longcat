// UIScene.js

class UIScene extends Phaser.Scene {
    constructor() {
        super('UIScene');
    }

    create() {
        this.scoreText = this.add.text(16, 16, 'Score: 0', { fontSize: '32px', fill: '#000' });

        // Listen for score updates
        this.registry.events.on('changedata', this.updateScore, this);
    }

    updateScore(parent, key, data) {
        if (key === 'score') {
            this.scoreText.setText('Score: ' + data);
        }
    }
}
