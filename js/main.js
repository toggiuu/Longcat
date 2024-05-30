// main.js

window.onload = function() {
    const config = {
        type: Phaser.AUTO,
        width: 800,
        height: 600,
        parent: 'game-container',
        scene: [PreloadScene, MenuScene, GameScene, UIScene, EndScene],
        physics: {
            default: 'arcade',
            arcade: {
                debug: false
            }
        }
    };

    const game = new Phaser.Game(config);
};
