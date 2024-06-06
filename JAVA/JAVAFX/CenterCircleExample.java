import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.stage.Stage;

public class CenterCircleExample extends Application {

    @Override
    public void start(Stage primaryStage) {
        // Create a circle with radius 50 and color blue
        Circle circle = new Circle(50, Color.BLUE);

        // Create a Pane and add the circle to it
        Pane root = new Pane(circle);

        // Bind the circle's center coordinates to the pane's center
        circle.centerXProperty().bind(root.widthProperty().divide(2));
        circle.centerYProperty().bind(root.heightProperty().divide(2));

        // Create a scene with the pane and set the stage
        Scene scene = new Scene(root, 400, 400);
        primaryStage.setTitle("Center Circle Example");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
