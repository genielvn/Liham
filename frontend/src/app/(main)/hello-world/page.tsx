import { Modal } from "@/components/Modal";

const HelloWorld = () => {
    return (
        <Modal
            title="Confirm Deletion"
            content="Are you sure you want to delete this?"
            okayAction={() => console.log("Deleted")}
            cancelAction={() => console.log("Cancelled")}
            okayText="Delete"
            cancelText="Cancel"
            type="warning"
        />
    );
};

export default HelloWorld;
