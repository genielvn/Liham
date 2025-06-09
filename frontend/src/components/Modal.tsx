import React from "react";
import style from "./Modal.module.scss";

interface ModalProps {
    title: string;
    content: string;
    okayAction: () => void;
    cancelAction: () => void;
    okayText: string;
    cancelText: string;
    type: "confirm" | "warning";
}

export const Modal: React.FC<ModalProps> = ({
    title,
    content,
    okayAction,
    cancelAction,
    okayText,
    cancelText,
    type,
}) => {
    const titleStyle =
        type === "confirm"
            ? style.confirm
            : type === "warning"
            ? style.warning
            : "";
    const buttonColor =
        type === "confirm" ? "pink" : type === "warning" ? "red" : "";

    return (
        <div className={style.modal}>
            <div className={style.modal__window}>
                <div>
                    <p className={`${style.modal__title} ${titleStyle}`}>
                        {title}
                    </p>
                    <p className={style.modal__content}>{content}</p>
                </div>
                <div className={style.modal__actions}>
                    <button
                        className={`btn-small btn-solid-${buttonColor}`}
                        onClick={okayAction}
                    >
                        {okayText}
                    </button>
                    <button
                        className={`btn-small btn-hollow-${buttonColor}`}
                        onClick={cancelAction}
                    >
                        {cancelText}
                    </button>
                </div>
            </div>
        </div>
    );
};
