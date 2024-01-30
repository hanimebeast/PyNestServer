# Flask Based Json-Server API

This is a simple Flask API for retrieving nested data from a JSON file.

## Video
[![json server usage by immodded](json-server.gif) ](json-server.webm) 

## Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/immodded/json-server.git
    cd json-server
    ```

2. **Install dependencies:**

    Ensure you have Python installed. Then install Flask using:

    ```bash
    pip install Flask
    ```

3. **Run the application:**

    Use the following command to run the Flask application:

    ```bash
    python main.py <json_file_path> [port]
    ```

    - `<json_file_path>`: Path to the JSON file you want to load.
    - `[port]` (optional): Port number to run the Flask application. Defaults to 7070 if not provided.

4. **Access the API:**

    - Open your web browser and navigate to `http://127.0.0.1:7070/` to see the entire JSON data.
    - To access nested data, use paths like `http://127.0.0.1:7070/key1/key2/key3`.

## API Endpoints

- `GET /`: Returns the entire JSON data.
- `GET /<path:keys>`: Returns the nested data at the specified path.

Example:

- `http://127.0.0.1:7070/` returns the entire JSON data.
- `http://127.0.0.1:7070/key1/2/key3::gt:69/keyx` returns the nested data at the specified path.
- `http://localhost:6001/from:1::to:5` return the list from index 1 to index 5
- `http://localhost:6001/from:3::` return the list from index 3 to last.
- `http://localhost:6001/::to:6` return the list from starting to 6.
- `http://localhost:6001/age::gt:20` return the list in which dictionary item has age[key] value greater than 20.
- `http://localhost:6001/age::lt:30` return the list in which dictionary item has age[key] value less than 30.
- `http://localhost:6001/id::et:3` return the list in which dictionary item has id[key] value equal to 3.

## Error Handling

- If an invalid path, index out of range, or trailing slash is detected, an error message will be returned in JSON format.

Example:

```json
{
  "error": "Invalid path, index out of range, or remove trailing slash."
}
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

