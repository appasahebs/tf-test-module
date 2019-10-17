
data "external" "image" {
  program = ["${path.module}/image.py", "image"]
  query = {
    namespace = "${var.namespace}"
  }
}
