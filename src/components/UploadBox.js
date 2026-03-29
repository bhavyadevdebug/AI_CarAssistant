export default function UploadBox() {
  return (
    <div className="border-dashed border-2 p-6 text-center rounded mb-6">
      <p>Drag and drop or click to upload a car lease document</p>
      <p className="text-sm text-gray-500">JPG, PNG, PDF — up to 20 MB</p>
      <button className="mt-4 bg-orange-500 text-white px-4 py-2 rounded">
        Browse Files
      </button>
    </div>
  );
}